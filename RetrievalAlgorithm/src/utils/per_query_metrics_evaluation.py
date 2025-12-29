import pandas as pd
from functools import reduce
from typing import Callable, List, Dict
from tqdm import tqdm
from concurrent.futures import ProcessPoolExecutor, as_completed
import os

from EvaluationMetrics.src.metrics import precision_at_k


def build_retrieval_index(scores_df: pd.DataFrame) -> Dict[str, List[str]]:
    scores_df_filtered = scores_df[scores_df['id_1'] != scores_df['id_2']]

    forward_df = (
        scores_df_filtered[['id_1', 'id_2', 'score']]
        .rename(columns={'id_1': 'query_id', 'id_2': 'other_id'})
    )

    backward_df = (
        scores_df_filtered[['id_2', 'id_1', 'score']]
        .rename(columns={'id_2': 'query_id', 'id_1': 'other_id'})
    )

    full_df = pd.concat([forward_df, backward_df], ignore_index=True)

    full_df = full_df.sort_values(
        ['query_id', 'score'], ascending=[True, False]
    )

    return (
        full_df
        .groupby('query_id')['other_id']
        .apply(list)
        .to_dict()
    )


def _eval_single_query(args):
    query_id, retrieved_list, k, eval_songs_df, genres_columns, metric_at_k = args
    return (
        query_id,
        metric_at_k(
            query_id=query_id,
            retrieved_ids=retrieved_list[:k],
            k=k,
            songs_df=eval_songs_df,
            genre_columns=genres_columns
        )
    )


def get_eval_metrics_for_each_query(
    scores_df: pd.DataFrame,
    k_range: List[int],
    eval_songs_df: pd.DataFrame,
    genres_columns: List[str],
    metric_at_k: Callable = precision_at_k,
    n_jobs: int = os.cpu_count()-2
) -> pd.DataFrame:

    if n_jobs is None:
        n_jobs = max(1, os.cpu_count() - 1)

    result_indices_dfs = []
    retrieval_index_dict = build_retrieval_index(scores_df=scores_df)

    for k in k_range:
        print('-' * 100)
        print('k =', k)

        tasks = [
            (query_id, retrieved_list, k, eval_songs_df, genres_columns, metric_at_k)
            for query_id, retrieved_list in retrieval_index_dict.items()
        ]

        results = {}

        with ProcessPoolExecutor(max_workers=n_jobs) as executor:
            futures = [executor.submit(_eval_single_query, t) for t in tasks]

            for future in tqdm(
                as_completed(futures),
                total=len(futures),
                desc=f'Evaluated Tracks at k={k}'
            ):
                query_id, score = future.result()
                results[query_id] = score

        result_indices_dfs.append(
            pd.DataFrame(list(results.items()), columns=['query_id', f'@k{k}'])
        )

    merged_df = reduce(
        lambda left, right: pd.merge(left, right, on='query_id'),
        result_indices_dfs
    )

    return merged_df
