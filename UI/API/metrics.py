""" Evaluation metrics """
import math
import ast

def get_genres_for_track(track_id, songs_df):
    """Extract genres from a track given its ID"""
    # Check if we have pre-parsed genres in a cache column
    if '_genre_set' in songs_df.columns:
        track_row = songs_df[songs_df['id'] == track_id]
        if not track_row.empty:
            return track_row['_genre_set'].iloc[0]
        return set()

    track_row = songs_df[songs_df['id'] == track_id]
    if track_row.empty:
        return set()
    
    genre_str = track_row['genre'].iloc[0]
    try:
        # Parse the string representation of a list
        genres_list = ast.literal_eval(genre_str)
        return set(genres_list)
    except (ValueError, SyntaxError, TypeError):
        return set()

def _ensure_genre_cache(songs_df):
    """Ensure the dataframe has a pre-parsed genre set column for performance"""
    if '_genre_set' not in songs_df.columns:
        def parse_genre(x):
            try:
                if isinstance(x, str):
                    return set(ast.literal_eval(x))
                return set(x) if isinstance(x, (list, set)) else set()
            except:
                return set()
        songs_df['_genre_set'] = songs_df['genre'].apply(parse_genre)

def is_relevant(query_id, retrieved_id, songs_df, genre_columns=None):
    """two tracks are relevant if they share at least one genre"""
    if query_id == retrieved_id:
        return False
    
    query_genres = get_genres_for_track(query_id, songs_df)
    retrieved_genres = get_genres_for_track(retrieved_id, songs_df)
    
    return len(query_genres & retrieved_genres) > 0


def precision_at_k(query_id, retrieved_ids, k, songs_df):
    """precision@k = number of relevant items / k"""
    if k <= 0:
        return 0.0
    
    if not retrieved_ids:
        return 0.0
    
    k = min(k, len(retrieved_ids))
    top_k = retrieved_ids[:k]
    
    query_genres = get_genres_for_track(query_id, songs_df)
    
    relevant_count = sum(
        1 for rid in top_k 
        if is_relevant(query_id, rid, songs_df, query_genres)
    )
    
    return relevant_count / k


def recall_at_k(query_id, retrieved_ids, k, songs_df):
    """recall@k = relevant items in top k / total relevant items in dataset"""
    if k <= 0 or not retrieved_ids:
        return 0.0
    
    _ensure_genre_cache(songs_df)
    
    query_genres = get_genres_for_track(query_id, songs_df)
    if not query_genres:
        return 0.0
    
    top_k = retrieved_ids[:min(k, len(retrieved_ids))]
    
    relevant_in_top_k = sum(
        1 for rid in top_k 
        if is_relevant(query_id, rid, songs_df, query_genres)
    )
    
    # Efficiently find total relevant in dataset (excluding query)
    total_relevant = songs_df.apply(
        lambda row: row['id'] != query_id and not query_genres.isdisjoint(row['_genre_set']), 
        axis=1
    ).sum()
    
    if total_relevant == 0:
        return 0.0
    
    return relevant_in_top_k / total_relevant


def mrr_at_k(query_id, retrieved_ids, k, songs_df):
    """MRR@k = 1 / position of first relevant item"""
    if k <= 0 or not retrieved_ids:
        return 0.0
    
    query_genres = get_genres_for_track(query_id, songs_df)
    top_k = retrieved_ids[:min(k, len(retrieved_ids))]
    
    for i, rid in enumerate(top_k):
        if is_relevant(query_id, rid, songs_df, query_genres):
            return 1.0 / (i + 1)
    
    return 0.0


def ndcg_at_k(query_id, retrieved_ids, k, songs_df):
    """nDCG@k = DCG@k / IDCG@k"""
    if k <= 0 or not retrieved_ids:
        return 0.0
    
    _ensure_genre_cache(songs_df)
    query_genres = get_genres_for_track(query_id, songs_df)
    if not query_genres:
        return 0.0
    
    k = min(k, len(retrieved_ids))
    top_k = retrieved_ids[:k]
    
    dcg = 0.0
    for i, rid in enumerate(top_k):
        rel = 1 if is_relevant(query_id, rid, songs_df, query_genres) else 0
        if rel > 0:
            dcg += rel / math.log2(i + 2)
    
    if dcg == 0.0:
        return 0.0
    
    # Efficiently find total relevant in dataset (excluding query)
    total_relevant = songs_df.apply(
        lambda row: row['id'] != query_id and not query_genres.isdisjoint(row['_genre_set']), 
        axis=1
    ).sum()
    
    ideal_relevant_count = min(k, total_relevant)
    
    idcg = 0.0
    for i in range(ideal_relevant_count):
        idcg += 1.0 / math.log2(i + 2)
    
    if idcg == 0.0:
        return 0.0
    
    return dcg / idcg


def coverage_at_k(all_retrieved_lists, k, total_items):
    """coverage@k = unique items recommended / total items in catalog"""
    unique_items = set()
    
    for ret_list in all_retrieved_lists:
        for item in ret_list[:k]:
            unique_items.add(item)
    
    if total_items == 0:
        return 0.0
    
    return len(unique_items) / total_items


def popularity_at_k(retrieved_ids, k, songs_df):
    """average popularity of top k items"""
    if 'popularity' not in songs_df.columns:
        return 0.0
    
    if not retrieved_ids:
        return 0.0
    
    top_k = retrieved_ids[:min(k, len(retrieved_ids))]
    if not top_k:
        return 0.0
    
    subset = songs_df[songs_df['id'].isin(top_k)]
    
    if subset.empty:
        return 0.0
    
    return subset['popularity'].mean()


def f1_at_k(query_id, retrieved_ids, k, songs_df):
    """F1@k = 2 * precision@k * recall@k / (precision@k + recall@k)"""
    precision = precision_at_k(query_id, retrieved_ids, k, songs_df)
    recall = recall_at_k(query_id, retrieved_ids, k, songs_df)
    
    if precision + recall == 0.0:
        return 0.0
    
    return 2 * precision * recall / (precision + recall)