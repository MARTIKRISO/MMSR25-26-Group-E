import pandas as pd
from tqdm import tqdm
from typing import List


def _order_id_pairs_in_df(df: pd.DataFrame) -> pd.DataFrame:
    return pd.DataFrame({
        'id_1': df[['id_1', 'id_2']].min(axis=1),
        'id_2': df[['id_1', 'id_2']].max(axis=1),
        'score': df['score']
    })


def _combine_score_dfs(score_dfs: List[pd.DataFrame]) -> pd.DataFrame:
    ordered_dfs = [_order_id_pairs_in_df(df) for df in tqdm(score_dfs, desc='Ordering ids in DataFrames')]

    merged_df = ordered_dfs[0]

    for i, df in tqdm(enumerate(ordered_dfs[1:], start=1), desc='Merging score DataFrames'):
        merged_df = merged_df.merge(
            df,
            on=['id_1', 'id_2'],
            how='inner',
            suffixes=(f'_{i-1}', f'_{i}'),
        )

    return merged_df


def _standard_normalize_df(df: pd.DataFrame) -> pd.DataFrame:
    df_normalized = df.copy()
    numeric_cols = df.select_dtypes(include='number').columns

    for col in tqdm(numeric_cols, desc='Normalizing numerical columns'):
        mean = df[col].mean()
        std = df[col].std()
        if std != 0:
            df_normalized[col] = (df[col] - mean) / std
        else:
            # if std = 0, set to 0 (avoid division by zero)
            df_normalized[col] = 0

    return df_normalized


def calculate_late_fusion_max_scores(score_dfs: List[pd.DataFrame]) -> pd.DataFrame:
    combined_df = _combine_score_dfs(score_dfs=score_dfs)
    normalized_df = _standard_normalize_df(df=combined_df)

    result_df = normalized_df[['id_1', 'id_2']].copy()
    result_df['score'] = normalized_df.drop(columns=['id_1', 'id_2']).max(axis=1)

    return result_df