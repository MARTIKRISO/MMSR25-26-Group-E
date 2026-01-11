""" Evaluation metrics """
import sys
import os
import math

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from EvaluationMetrics.src.data_loader import get_genres_for_track, get_genre_columns

def is_relevant(query_id, retrieved_id, songs_df, genre_columns):
    """two tracks are relevant if they share at least one genre"""
    if query_id == retrieved_id:
        return False
    
    query_genres = get_genres_for_track(query_id, songs_df, genre_columns)
    retrieved_genres = get_genres_for_track(retrieved_id, songs_df, genre_columns)
    
    return len(query_genres & retrieved_genres) > 0


def precision_at_k(query_id, retrieved_ids, k, songs_df, genre_columns):
    """precision@k = number of relevant items / k"""
    if k <= 0:
        raise ValueError("k must be positive")
    
    if not retrieved_ids:
        return 0.0
    
    k = min(k, len(retrieved_ids))
    if k == 0:
        return 0.0
    
    top_k = retrieved_ids[:k]
    
    relevant_count = sum(
        1 for rid in top_k 
        if is_relevant(query_id, rid, songs_df, genre_columns)
    )
    
    return relevant_count / k


def recall_at_k(query_id, retrieved_ids, k, songs_df, genre_columns):
    """recall@k = relevant items in top k / total relevant items in dataset"""
    if k <= 0:
        return 0.0
    
    if not retrieved_ids:
        return 0.0
    
    k = min(k, len(retrieved_ids))
    if k == 0:
        return 0.0
    
    top_k = retrieved_ids[:k]
    
    query_genres = get_genres_for_track(query_id, songs_df, genre_columns)
    if not query_genres:
        return 0.0
    
    relevant_in_top_k = sum(
        1 for rid in top_k 
        if is_relevant(query_id, rid, songs_df, genre_columns)
    )
    
    # find total relevant in dataset (excluding query)
    genre_matrix = songs_df[list(query_genres)]
    relevant_mask = genre_matrix.sum(axis=1) > 0
    relevant_mask = relevant_mask & (songs_df['id'] != query_id)
    total_relevant = relevant_mask.sum()
    
    if total_relevant == 0:
        return 0.0
    
    return relevant_in_top_k / total_relevant


def mrr_at_k(query_id, retrieved_ids, k, songs_df, genre_columns):
    """MRR@k = 1 / position of first relevant item"""
    if k <= 0:
        return 0.0
    
    if not retrieved_ids:
        return 0.0
    
    top_k = retrieved_ids[:min(k, len(retrieved_ids))]
    
    for i, rid in enumerate(top_k):
        if is_relevant(query_id, rid, songs_df, genre_columns):
            return 1.0 / (i + 1)
    
    return 0.0


def ndcg_at_k(query_id, retrieved_ids, k, songs_df, genre_columns):
    """nDCG@k = DCG@k / IDCG@k"""
    if k <= 0:
        return 0.0
    
    if not retrieved_ids:
        return 0.0
    
    k = min(k, len(retrieved_ids))
    if k == 0:
        return 0.0
    
    top_k = retrieved_ids[:k]
    
    dcg = 0.0
    for i, rid in enumerate(top_k):
        rel = 1 if is_relevant(query_id, rid, songs_df, genre_columns) else 0
        if rel > 0:
            dcg += rel / math.log2(i + 2)
    
    if dcg == 0.0:
        return 0.0
    
    query_genres = get_genres_for_track(query_id, songs_df, genre_columns)
    if not query_genres:
        return 0.0
    
    genre_matrix = songs_df[list(query_genres)]
    relevant_mask = genre_matrix.sum(axis=1) > 0
    relevant_mask = relevant_mask & (songs_df['id'] != query_id)
    total_relevant = relevant_mask.sum()
    
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


if __name__ == "__main__":
    from EvaluationMetrics.src.data_loader import load_songs_data, get_genre_columns
    
    print("Loading data...")
    df = load_songs_data()
    genres = get_genre_columns()
    
    query = df.iloc[0]['id']
    retrieved = [df.iloc[i]['id'] for i in range(1, 11)]
    
    print(f"\nQuery: {query}")
    print(f"Query genres: {get_genres_for_track(query, df, genres)}")
    print(f"\nTesting with k=10")
    print("\n")
    
    k = 10
    
    p = precision_at_k(query, retrieved, k, df, genres)
    print(f"Precision@{k}: {p:.4f}")
    
    r = recall_at_k(query, retrieved, k, df, genres)
    print(f"Recall@{k}: {r:.4f}")
    
    mrr = mrr_at_k(query, retrieved, k, df, genres)
    print(f"MRR@{k}: {mrr:.4f}")
    
    ndcg = ndcg_at_k(query, retrieved, k, df, genres)
    print(f"nDCG@{k}: {ndcg:.4f}")
    
    print("\n")
    print("Testing Coverage")
    all_retrieved = []
    for i in range(5):
        ret = [df.iloc[j]['id'] for j in range(i+1, i+11)]
        all_retrieved.append(ret)
    
    cov = coverage_at_k(all_retrieved, k=10, total_items=len(df))
    print(f"Coverage@10: {cov:.4f}")
    
    print("\n")
    print("Testing edge cases")
    p_empty = precision_at_k(query, [], 10, df, genres)
    print(f"Empty list: {p_empty:.4f}")
    
    short = [df.iloc[1]['id'], df.iloc[2]['id']]
    p_short = precision_at_k(query, short, 10, df, genres)
    print(f"k>len: {p_short:.4f}")
    
    print("\n")
    print("All metrics working!")