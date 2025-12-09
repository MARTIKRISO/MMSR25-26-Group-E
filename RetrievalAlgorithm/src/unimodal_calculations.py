import os
import pandas as pd
from tqdm import tqdm
from typing import Type

import torch
from torch.utils.data import DataLoader
from RetrievalAlgorithm.src.datasets import UnimodalPairedTracksDataset
from RetrievalAlgorithm.src.normalization import NormalizationModule
from RetrievalAlgorithm.src.score_calculation_modules.cosine_similarity_module import CosineSimilarityModule


def calculate_unimodal_similarity(
                                    dataset_df: pd.DataFrame,
                                    calculation_module: CosineSimilarityModule,
                                    normalization_module_type: Type[NormalizationModule] = NormalizationModule,
                                    feature_name: str = 'Lyrics',
                                    batch_size: int = 512,
                                    include_self_pairs: bool = True,
                                    include_reverse_pairs: bool = True,
                                  ) -> pd.DataFrame:
        device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        calculation_module.to(device)
        calculation_module.eval()

        num_workers = max(2, os.cpu_count()-2)
        calculation_dataset = UnimodalPairedTracksDataset(
            dataset_df=dataset_df,
            include_self_pairs=include_self_pairs,
            include_reverse_pairs=include_reverse_pairs,
        )

        normalization_module = normalization_module_type()
        normalization_module.fit(calculation_dataset.features)
        normalization_module.to(device)
        normalization_module = torch.jit.script(normalization_module)

        calculation_dataloader = DataLoader(
            dataset=calculation_dataset,
            batch_size=batch_size,
            pin_memory=torch.cuda.is_available(),
            num_workers=num_workers,
            shuffle=False,
        )

        results = {
            'id_1': [],
            'id_2': [],
            f'{feature_name}_similarity': torch.empty(0).to(device),
        }

        with torch.no_grad():
            for (id_1_batch, feature_1_batch, id_2_batch, feature_2_batch) in tqdm(calculation_dataloader, desc='Batches', unit='it'):
                results['id_1'].extend(list(id_1_batch))
                results['id_2'].extend(list(id_2_batch))

                feature_1_batch = feature_1_batch.to(device)
                feature_2_batch = feature_2_batch.to(device)

                feature_1_batch = normalization_module(feature_1_batch)
                feature_2_batch = normalization_module(feature_2_batch)

                sim_scores_batch = calculation_module(feature_1_batch, feature_2_batch)
                sim_scores_batch = sim_scores_batch.view(-1)  # flatten to 1D
                results[f'{feature_name}_similarity'] = torch.cat(
                    [results[f'{feature_name}_similarity'], sim_scores_batch],
                    dim=0
                ).cpu()
                del feature_1_batch, feature_2_batch, sim_scores_batch

        if torch.cuda.is_available():
            torch.cuda.empty_cache()
        results[f'{feature_name}_similarity'] = results[f'{feature_name}_similarity']

        return pd.DataFrame(results)