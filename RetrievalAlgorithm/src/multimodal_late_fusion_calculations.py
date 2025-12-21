import pandas as pd
from typing import List
from RetrievalAlgorithm.src.utils.df_processing import _combine_score_dfs, _standardize_df


def calculate_late_fusion_max_scores(score_dfs: List[pd.DataFrame]) -> pd.DataFrame:
    combined_df = _combine_score_dfs(score_dfs=score_dfs)
    standard_df = _standardize_df(df=combined_df)

    result_df = standard_df[['id_1', 'id_2']].copy()
    result_df['score'] = standard_df.drop(columns=['id_1', 'id_2']).max(axis=1)

    return result_df