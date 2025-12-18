import os
import pandas as pd
from tqdm import tqdm
from typing import List, Type

import torch
from torch.utils.data import DataLoader
from RetrievalAlgorithm.src.normalization import NormalizationModule
from RetrievalAlgorithm.src.datasets import MultimodalPairedTracksDataset
from RetrievalAlgorithm.src.score_calculation_modules.cosine_similarity_module import CosineSimilarityModule


def calculate_multimodal_similarity(
                                    datasets_df: List[pd.DataFrame],
                                    calculation_module: CosineSimilarityModule,
                                    normalization_module_type: Type[NormalizationModule] = NormalizationModule,
                                    batch_size: int = 512,
                                    include_self_pairs: bool = False,
                                    include_reverse_pairs: bool = False,
                                  ) -> pd.DataFrame:
        device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        calculation_module.to(device)
        calculation_module.eval()

        num_workers = 0 if torch.cuda.is_available() else max(2, os.cpu_count() - 2)
        calculation_dataset = MultimodalPairedTracksDataset(
            datasets_df=datasets_df,
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
            'score': [],
        }

        with torch.no_grad():
            for (id_1_batch, feature_1_batch, id_2_batch, feature_2_batch) in tqdm(calculation_dataloader, desc='Batches', unit='it'):
                results['id_1'].extend(list(id_1_batch))
                results['id_2'].extend(list(id_2_batch))

                feature_1_batch = feature_1_batch.to(device)
                feature_2_batch = feature_2_batch.to(device)

                with torch.amp.autocast(device_type=device.type):
                    feature_1_batch = normalization_module(feature_1_batch)
                    feature_2_batch = normalization_module(feature_2_batch)
                    sim_scores_batch = calculation_module(feature_1_batch, feature_2_batch).view(-1)

                results['score'].append(sim_scores_batch)
                del feature_1_batch, feature_2_batch, sim_scores_batch

        results['score'] = torch.cat(results['score']).cpu()
        if torch.cuda.is_available():
            torch.cuda.empty_cache()
        results[f'score'] = results[f'score']

        return pd.DataFrame(results)