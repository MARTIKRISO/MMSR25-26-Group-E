import pandas as pd
from typing import List
from RetrievalAlgorithm.src.utils.df_processing import _combine_score_dfs, _standardize_df


def calculate_late_fusion_max_scores(score_dfs: List[pd.DataFrame]) -> pd.DataFrame:
    combined_df = _combine_score_dfs(score_dfs=score_dfs)
    standard_df = _standardize_df(df=combined_df)

    result_df = standard_df[['id_1', 'id_2']].copy()
    result_df['score'] = standard_df.drop(columns=['id_1', 'id_2']).max(axis=1)

    return result_df


def _get_rank_pairs_df(scores_df: pd.DataFrame) -> pd.DataFrame:
    # Create bidirectional (query, target) pairs
    df_forward = scores_df.rename(columns={'id_1': 'query', 'id_2': 'target'})
    df_backward = scores_df.rename(columns={'id_2': 'query', 'id_1': 'target'})
    # Prevent self pairs to be included twice
    df_backward = df_backward[df_backward['query'] != df_backward['target']]

    df = pd.concat([df_forward, df_backward], ignore_index=True)

    # Rank numeric score columns per query
    score_cols = df.select_dtypes(include='number').columns

    for col in score_cols:
        df[f'{col}_rank'] = (
            df.groupby('query')[col]
              .rank(method='first', ascending=False)
              .astype('int32')
                      - 1
        )
    return df


def calculate_late_fusion_rrf_scores(score_dfs: List[pd.DataFrame], k: int = 60) -> pd.DataFrame:
    combined_df = _combine_score_dfs(score_dfs=score_dfs)
    standard_df = _standardize_df(df=combined_df)

    ranked_pairs_df = _get_rank_pairs_df(scores_df=standard_df)

    rrf_result_df = ranked_pairs_df[['query', 'target']].copy()
    rrf_result_df['score'] = (1 / (k + rrf_result_df.filter(like='_rank'))).sum(axis=1)
    return rrf_result_df