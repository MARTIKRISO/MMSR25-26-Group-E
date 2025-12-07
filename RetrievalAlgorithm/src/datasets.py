import pandas as pd
from typing import Tuple, List
import torch
from torch.utils.data import Dataset
import itertools
from functools import reduce


def _generate_pairs(
        all_indices: List[int],
        include_self_pairs: bool = False,
        include_reverse_pairs: bool = False,
    ) -> torch.Tensor:
    if include_self_pairs and include_reverse_pairs:
        return torch.tensor(
            list(itertools.product(all_indices, all_indices)),
            dtype=torch.long
        )

    if include_self_pairs and not include_reverse_pairs:
        return torch.tensor(
            list(itertools.combinations_with_replacement(all_indices, r=2)),
            dtype=torch.long
        )

    if not include_self_pairs and include_reverse_pairs:
        return torch.tensor(
            [(i, j) for i in all_indices for j in all_indices if i != j],
            dtype=torch.long
        )

    return torch.tensor(
        list(itertools.combinations(all_indices, r=2)),
        dtype=torch.long
    )


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
        all_indices = list(range(len(self.ids)))
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
        all_indices = list(range(len(self.ids)))
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
