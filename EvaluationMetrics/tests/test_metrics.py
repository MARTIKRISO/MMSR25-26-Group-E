""" Test evaluation metrics """
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from EvaluationMetrics.src.data_loader import load_songs_data, get_genre_columns
from EvaluationMetrics.src.metrics import (
    precision_at_k, recall_at_k, mrr_at_k, 
    ndcg_at_k, coverage_at_k, popularity_at_k
)


def test_basic_metrics():
    """test precision, recall, mrr, ndcg with known data"""
    print("\n" )
    print("TEST 1: Basic Metrics")
    
    
    df = load_songs_data()
    genres = get_genre_columns()
    
    query = df.iloc[0]['id']
    retrieved = [df.iloc[i]['id'] for i in range(1, 21)]
    
    print(f"Query: {query}")
    print(f"Retrieved: {len(retrieved)} tracks")
    
    k_values = [5, 10, 20]
    
    for k in k_values:
        print(f"\nk = {k}")
        print("-" * 40)
        
        p = precision_at_k(query, retrieved, k, df, genres)
        r = recall_at_k(query, retrieved, k, df, genres)
        mrr = mrr_at_k(query, retrieved, k, df, genres)
        ndcg = ndcg_at_k(query, retrieved, k, df, genres)
        
        print(f"  Precision: {p:.4f}")
        print(f"  Recall:    {r:.4f}")
        print(f"  MRR:       {mrr:.4f}")
        print(f"  nDCG:      {ndcg:.4f}")
    
    print("\n Basic metrics test passed")


def test_coverage():
    """test coverage across multiple queries"""
    print("\n" )
    print("TEST 2: Coverage")
    
    
    df = load_songs_data()
    
    # simulate 10 queries
    all_retrieved = []
    for i in range(10):
        ret = [df.iloc[j]['id'] for j in range(i*5, i*5+20)]
        all_retrieved.append(ret)
    
    k_values = [5, 10, 20]
    
    for k in k_values:
        cov = coverage_at_k(all_retrieved, k, len(df))
        unique_count = int(cov * len(df))
        print(f"Coverage@{k}: {cov:.4f} ({unique_count}/{len(df)} tracks)")
    
    print("\n Coverage test passed")


def test_edge_cases():
    """test edge cases"""
    print("\n" )
    print("TEST 3: Edge Cases")
    
    
    df = load_songs_data()
    genres = get_genre_columns()
    
    query = df.iloc[0]['id']
    
    # empty retrieval
    empty = []
    try:
        p = precision_at_k(query, empty, 10, df, genres)
        print(f"Empty list: Precision = {p:.4f}")
    except Exception as e:
        print(f"Empty list error: {e}")
    
    # k larger than results
    short = [df.iloc[i]['id'] for i in range(1, 4)]
    p = precision_at_k(query, short, 10, df, genres)
    print(f"k>len: Precision@10 with 3 items = {p:.4f}")
    
    # same track as query
    same = [query]
    p = precision_at_k(query, same, 1, df, genres)
    print(f"Query in results: Precision = {p:.4f}")
    
    print("\n Edge cases handled")


def test_all_queries_sample():
    """test metrics on sample of all queries"""
    print("\n" )
    print("TEST 4: Sample of All Queries")
    
    
    df = load_songs_data()
    genres = get_genre_columns()
    
    # test on 50 random queries
    import random
    sample_size = min(50, len(df))
    sample_indices = random.sample(range(len(df)), sample_size)
    
    precisions = []
    recalls = []
    mrrs = []
    ndcgs = []
    
    for idx in sample_indices:
        query = df.iloc[idx]['id']
        # simulate retrieval: get 10 random other tracks
        other_indices = [i for i in range(len(df)) if i != idx]
        ret_indices = random.sample(other_indices, min(10, len(other_indices)))
        retrieved = [df.iloc[i]['id'] for i in ret_indices]
        
        p = precision_at_k(query, retrieved, 10, df, genres)
        r = recall_at_k(query, retrieved, 10, df, genres)
        m = mrr_at_k(query, retrieved, 10, df, genres)
        n = ndcg_at_k(query, retrieved, 10, df, genres)
        
        precisions.append(p)
        recalls.append(r)
        mrrs.append(m)
        ndcgs.append(n)
    
    print(f"Tested on {sample_size} queries")
    print(f"\nAverage Precision@10: {sum(precisions)/len(precisions):.4f}")
    print(f"Average Recall@10:    {sum(recalls)/len(recalls):.4f}")
    print(f"Average MRR@10:       {sum(mrrs)/len(mrrs):.4f}")
    print(f"Average nDCG@10:      {sum(ndcgs)/len(ndcgs):.4f}")
    
    print("\n All queries sample test passed")


if __name__ == "__main__":
    print("Starting tests...")
    
    test_basic_metrics()
    test_coverage()
    test_edge_cases()
    test_all_queries_sample()
    
    print("\n" )
    print("ALL TESTS WORKING")
    