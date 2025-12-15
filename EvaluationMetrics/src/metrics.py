""" Evaluation metrics """
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from EvaluationMetrics.src.data_loader import get_genres_for_track, get_genre_columns

def is_relevant(query_id, retrieved_id, songs_df, genre_columns):
    """two tracks are relevant if they share at least one genre """

    if query_id == retrieved_id:
        return False  # same track is not relevant
    
    query_genres = get_genres_for_track(query_id, songs_df, genre_columns)
    retrieved_genres = get_genres_for_track(retrieved_id, songs_df, genre_columns)
    
    # true if share at least 1 genre
    return len(query_genres & retrieved_genres) > 0


def precision_at_k(query_id, retrieved_ids, k, songs_df, genre_columns):
    """
    precision@k = number of relevant items / k
    return precision@k value
    """
    if k <= 0:
        raise ValueError("k must be positive")
    
    if len(retrieved_ids) < k:
        print(f"Warning: Only {len(retrieved_ids)} results available, but k={k}")
        k = len(retrieved_ids)
    
    top_k = retrieved_ids[:k]
    
    # Count how many are relevant
    relevant_count = sum(
        1 for rid in top_k 
        if is_relevant(query_id, rid, songs_df, genre_columns)
    )
    
    return relevant_count / k


# TODO: Implement other metrics
def recall_at_k(query_id, retrieved_ids, k, songs_df, genre_columns):
    """calculate Recall@k - TO BE IMPLEMENTED"""
    pass

def mrr_at_k(query_id, retrieved_ids, k, songs_df, genre_columns):
    """calculate MRR@k - TO BE IMPLEMENTED"""
    pass

def ndcg_at_k(query_id, retrieved_ids, k, songs_df, genre_columns):
    """calculate nDCG@k - TO BE IMPLEMENTED"""
    pass

def coverage_at_k(all_retrieved_lists, k, total_items):
    """calculate Coverage@k - TO BE IMPLEMENTED"""
    pass

def popularity_at_k(retrieved_ids, k, songs_df):
    """calculate Pop@k - TO BE IMPLEMENTED"""
    pass


if __name__ == "__main__":
    # simple test
    from EvaluationMetrics.src.data_loader import load_songs_data, get_genre_columns
    
    print("Loading data...")
    df = load_songs_data()
    genres = get_genre_columns()
    
    # test with first 4 tracks
    query = df.iloc[0]['id']
    retrieved = [df.iloc[1]['id'], df.iloc[2]['id'], df.iloc[3]['id']]
    
    print(f"\nQuery track: {query}")
    print(f"Query genres: {get_genres_for_track(query, df, genres)}")
    print(f"\nRetrieved tracks: {retrieved}")
    
    p_at_3 = precision_at_k(query, retrieved, k=3, songs_df=df, genre_columns=genres)
    print(f"\nPrecision@3: {p_at_3:.3f}")
    
    # check each track individually
    print("\nDetailed relevance check:")
    for rid in retrieved:
        rel = is_relevant(query, rid, df, genres)
        track_genres = get_genres_for_track(rid, df, genres)
        print(f"  {rid}: {'+ relevant' if rel else 'x not relevant'} - genres: {track_genres}")
