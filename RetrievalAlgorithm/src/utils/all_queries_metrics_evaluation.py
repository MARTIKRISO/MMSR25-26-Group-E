import os

import pandas as pd
from typing import List, Callable, Dict
from tqdm import tqdm

from RetrievalAlgorithm.src.utils.per_query_metrics_evaluation import get_eval_metrics_for_each_query, get_rrf_eval_metrics_for_each_query

norm_names = ['raw', 'min_max', 'max_abs', 'robust', 'standard']


def _calculate_and_save_unimodal_metric(feature_name: str,
                                        target_dir: str,
                                        eval_songs_df: pd.DataFrame,
                                        genres_columns: List[str],
                                        metric_at_k: Callable,
                                        metric_at_k_name: str) -> None:
    os.makedirs(target_dir, exist_ok=True)

    for norm_name in norm_names:
        output_norm_dir = os.path.join(target_dir, norm_name)
        output_path = os.path.join(output_norm_dir,
                                   metric_at_k_name,
                                   f'unimodal_{norm_name}_{feature_name}_{metric_at_k_name}.parquet')
        if os.path.exists(output_path):
            print(f'Skipping {norm_name}')
            continue

        scores_path = f'{target_dir}/{norm_name}/unimodal_{norm_name}_{feature_name}_similarity_scores.parquet'
        precalculated_scores_df = pd.read_parquet(scores_path)

        print('='*100)
        print('Normalization Name:', norm_name, '\n')

        eval_score_df = get_eval_metrics_for_each_query(
            scores_df=precalculated_scores_df,
            k_range=[5, 10, 20, 50, 100, 200],
            genres_columns=genres_columns,
            eval_songs_df=eval_songs_df,
            metric_at_k=metric_at_k
        )
        os.makedirs(output_norm_dir, exist_ok=True)

        eval_score_df.to_parquet(output_path, index=False)


def _calculate_and_save_multimodal_metric(
        feature_name: str,
        target_dir: str,
        eval_songs_df: pd.DataFrame,
        genres_columns: List[str],
        metric_at_k: Callable,
        metric_at_k_name: str
) -> None:
    os.makedirs(target_dir, exist_ok=True)

    for norm_name in norm_names:
        output_norm_dir = os.path.join(target_dir, norm_name)
        output_path = os.path.join(output_norm_dir,
                                   metric_at_k_name,
                                   f'multimodal_{norm_name}_{feature_name}_{metric_at_k_name}.parquet')
        if os.path.exists(output_path):
            print(f'Skipping {norm_name}')
            continue

        scores_path = os.path.join(target_dir, norm_name, f'multimodal_{norm_name}_{feature_name}_similarity_scores.parquet')
        precalculated_scores_df = pd.read_parquet(scores_path)

        print('='*100)
        print('Normalization Name:', norm_name, '\n')

        eval_score_df = get_eval_metrics_for_each_query(
            scores_df=precalculated_scores_df,
            k_range=[5, 10, 20, 50, 100, 200],
            genres_columns=genres_columns,
            eval_songs_df=eval_songs_df,
            metric_at_k=metric_at_k
        )
        os.makedirs(output_norm_dir, exist_ok=True)

        eval_score_df.to_parquet(output_path, index=False)


def _calculate_and_save_multimodal_max_score_metric(
        target_dir: str,
        eval_songs_df: pd.DataFrame,
        genres_columns: List[str],
        metric_at_k: Callable,
        metric_at_k_name: str
) -> Dict[str, pd.DataFrame]:
    os.makedirs(target_dir, exist_ok=True)

    metric_dfs: Dict[str, pd.DataFrame] = {}
    os.makedirs(target_dir, exist_ok=True)

    print(f'Loading Max Score precalculated similarity scores ...')

    for norm_name in tqdm(norm_names, desc='Loading precalculated scores'):
        scores_path = os.path.join(
            target_dir,
            f'multimodal_{norm_name}_max_similarity_scores.parquet'
        )
        output_path = os.path.join(
            target_dir,
            metric_at_k_name,
            f'multimodal_{norm_name}_max_{metric_at_k_name}.parquet'
        )

        if os.path.exists(output_path):
            print(f'Skipping {norm_name}')
            continue

        precalculated_scores_df = pd.read_parquet(scores_path)

        print('=' * 100)
        print('Normalization Name:', norm_name, '\n')

        metric_dfs[norm_name] = get_eval_metrics_for_each_query(
            scores_df=precalculated_scores_df,
            k_range=[5, 10, 20, 50, 100, 200],
            genres_columns=genres_columns,
            eval_songs_df=eval_songs_df,
            metric_at_k=metric_at_k
        )
        metric_dfs[norm_name].to_parquet(output_path, index=False)


def _calculate_and_save_rrf_metric(
        target_dir: str,
        eval_songs_df: pd.DataFrame,
        genres_columns: List[str],
        metric_at_k: Callable,
        metric_at_k_name: str,
        k_range: List[int] = [5, 10, 20, 50, 100, 200]
) -> None:
    os.makedirs(target_dir, exist_ok=True)

    print('Loading RRF similarity scores ...')

    for norm_name in norm_names:
        scores_path = os.path.join(
            target_dir,
            f'multimodal_{norm_name}_rrf_similarity_scores.parquet'
        )

        output_path = os.path.join(
            target_dir,
            metric_at_k_name,
            f'rff_{norm_name}_{metric_at_k_name}.parquet'
        )

        if os.path.exists(output_path):
            print(f'Skipping {norm_name}')
            continue

        print('=' * 100)
        print('Normalization Name:', norm_name, '\n')

        precalculated_scores_df = pd.read_parquet(scores_path)

        eval_score_df = get_rrf_eval_metrics_for_each_query(
            scores_df=precalculated_scores_df,
            k_range=k_range,
            genres_columns=genres_columns,
            eval_songs_df=eval_songs_df,
            metric_at_k=metric_at_k
        )

        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        eval_score_df.to_parquet(output_path, index=False)



def _calculate_and_save_nn_based_metric(
        target_dir: str,
        eval_songs_df: pd.DataFrame,
        genres_columns: List[str],
        metric_at_k: Callable,
        metric_at_k_name: str
) -> None:
    os.makedirs(target_dir, exist_ok=True)

    metric_dfs: Dict[str, pd.DataFrame] = {}

    print('Loading NN-based similarity scores ...')

    variation_names = [
        'max_scores', 'avg_scores'
    ]
    feature_names = [
        'lyrics_bert_lyrics_bert_padding', 'lyrics_bert_mfcc_bow_padding', 'mfcc_bow_mfcc_bow_padding',
        'vgg19_lyrics_bert_padding', 'vgg19_mfcc_bow_padding', 'vgg19_vgg19_padding',
    ]

    for variation_name in variation_names:
        print('='*100)
        print('Variation Name:', variation_name)

        for feature_name in feature_names:
            scores_path = os.path.join(
                target_dir,
                variation_name,
                f'NN_based_{feature_name}_{variation_name}.parquet'
            )
            output_path = os.path.join(
                target_dir,
                variation_name,
                metric_at_k_name,
            )

            os.makedirs(output_path, exist_ok=True)

            output_path = os.path.join(
                output_path,
                f'NN_based_{feature_name}_{variation_name}_{metric_at_k_name}.parquet'
            )

            if os.path.exists(output_path):
                print(f'Skipping {variation_name}/{feature_name}')
                continue

            precalculated_scores_df = pd.read_parquet(scores_path)

            print('-' * 100)
            print('Feature Name:', feature_name, '\n')

            metric_dfs[feature_name] = get_eval_metrics_for_each_query(
                scores_df=precalculated_scores_df,
                k_range=[5, 10, 20, 50, 100, 200],
                genres_columns=genres_columns,
                eval_songs_df=eval_songs_df,
                metric_at_k=metric_at_k
            )

            metric_dfs[feature_name].to_parquet(output_path, index=False)
