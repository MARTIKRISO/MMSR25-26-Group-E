import pandas as pd
from typing import Tuple, List
import torch
from torch.utils.data import Dataset
from functools import reduce


def _generate_pairs(
    all_indices: torch.Tensor,
    include_self_pairs: bool = False,
    include_reverse_pairs: bool = False
) -> torch.Tensor:
    n = all_indices.size(0)

    # Create a grid of indices
    i = all_indices.view(-1, 1).expand(-1, n)
    j = all_indices.view(1, -1).expand(n, -1)

    if include_self_pairs and include_reverse_pairs:
        # All pairs (i,j)
        pairs = torch.stack((i.flatten(), j.flatten()), dim=1)
        return pairs

    if include_self_pairs and not include_reverse_pairs:
        # Upper triangular including diagonal
        mask = torch.triu(torch.ones(n, n, dtype=torch.bool))
        pairs = torch.stack((i[mask], j[mask]), dim=1)
        return pairs

    if not include_self_pairs and include_reverse_pairs:
        # Remove diagonal
        mask = ~torch.eye(n, dtype=torch.bool)
        pairs = torch.stack((i[mask], j[mask]), dim=1)
        return pairs

    # No self pairs, no reverse pairs: upper triangular without diagonal
    mask = torch.triu(torch.ones(n, n, dtype=torch.bool), diagonal=1)
    pairs = torch.stack((i[mask], j[mask]), dim=1)
    return pairs


class UnimodalPairedTracksDataset(Dataset):
    def __init__(
        self,
        dataset_df: pd.DataFrame,
        include_self_pairs: bool = False,
        include_reverse_pairs: bool = False,
    ) -> None:
        super().__init__()
        self.ids = dataset_df['id'].tolist()
        self.idx_to_id = {i: id_ for i, id_ in enumerate(self.ids)}

        self.features = torch.tensor(
            dataset_df.drop(columns=['id']).values,
            dtype=torch.float32,
        )

        if torch.cuda.is_available():
            self.features = self.features.pin_memory()

        all_indices = torch.arange(len(self.ids))
        self.pairs = _generate_pairs(
            all_indices=all_indices,
            include_self_pairs=include_self_pairs,
            include_reverse_pairs=include_reverse_pairs
        )

    def __len__(self) -> int:
        return len(self.pairs)

    def __getitem__(self, idx: int) -> Tuple[str, torch.Tensor, str, torch.Tensor]:
        i, j = self.pairs[idx]

        feat1 = self.features[i]
        feat2 = self.features[j]

        return self.idx_to_id[i.item()],feat1, self.idx_to_id[j.item()], feat2


class MultimodalPairedTracksDataset(Dataset):
    def __init__(self,
                 datasets_df: List[pd.DataFrame],
                 include_self_pairs: bool = False,
                 include_reverse_pairs: bool = False
    ) -> None:
        super().__init__()
        merged_df = reduce(lambda left, right: left.merge(right, on='id'), datasets_df)

        self.ids = merged_df['id'].tolist()
        self.idx_to_id = {i: id_ for i, id_ in enumerate(self.ids)}

        self.features = torch.tensor(
            merged_df.drop(columns=['id']).values,
            dtype=torch.float32,
        )

        if torch.cuda.is_available():
            self.features = self.features.pin_memory()

        all_indices = torch.arange(len(self.ids))
        self.pairs = _generate_pairs(
            all_indices=all_indices,
            include_self_pairs=include_self_pairs,
            include_reverse_pairs=include_reverse_pairs
        )

    def __len__(self) -> int:
        return len(self.pairs)

    def __getitem__(self, idx: int) -> Tuple[str, torch.Tensor, str, torch.Tensor]:
        i, j = self.pairs[idx]

        feat1 = self.features[i]
        feat2 = self.features[j]

        return self.idx_to_id[i.item()],feat1, self.idx_to_id[j.item()], feat2


if __name__ == '__main__':
    from RetrievalAlgorithm.src.utils.data_loading import _load_one_tsv_file

    # Unimodal
    _, test_df = _load_one_tsv_file(file_path='../../Dataset/id_lyrics_bert_mmsr.tsv')

    bert_dataset = UnimodalPairedTracksDataset(dataset_df=test_df)
    id_1, feature_1, id_2, feature_2 = bert_dataset[0]

    print('='*100)
    print('Dataset Class: UnimodalPairedTracksDataset')
    print(' Dataset Size = ', len(bert_dataset))
    print(' Pair ID = ', 0)
    print('     1. Track_ID = ', id_1)
    print('         Features type = ', type(feature_1))
    print('         Features size = ', feature_1.size())
    print('     2. Track_ID = ', id_2)
    print('         Features type = ', type(feature_2))
    print('         Features size = ', feature_2.size())


    # Multimodal
    _, lyrics_df = _load_one_tsv_file(file_path='../../Dataset/id_lyrics_bert_mmsr.tsv')
    _, mfcc_bow_df = _load_one_tsv_file(file_path='../../Dataset/id_mfcc_bow_mmsr.tsv')
    _, vgg_df = _load_one_tsv_file(file_path='../../Dataset/id_vgg19_mmsr.tsv')

    multimodal_dataset = MultimodalPairedTracksDataset(datasets_df=[lyrics_df, mfcc_bow_df, vgg_df])
    id_1, feature_1, id_2, feature_2 = multimodal_dataset[0]

    print('\n')
    print('='*100)
    print('Dataset Class: MultimodalPairedTracksDataset')
    print(' Dataset Size = ', len(multimodal_dataset))
    print(' Pair ID = ', 0)
    print('     1. Track_ID = ', id_1)
    print('         Features type = ', type(feature_1))
    print('         Features size = ', feature_1.size())
    print('     2. Track_ID = ', id_2)
    print('         Features type = ', type(feature_2))
    print('         Features size = ', feature_2.size())
