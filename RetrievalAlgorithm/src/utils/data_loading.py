import pandas as pd
import os, glob

from typing import Dict, Tuple
from tqdm import tqdm
from joblib import Parallel, delayed


def _load_one_tsv_file(file_path: str) -> Tuple[str, pd.DataFrame]:
    """
    :param file_path: the path to the .tsv file you want to load
    :return: a Tuple of the file path and the dataframe loaded from the .tsv file
    """
    name = os.path.basename(file_path)
    df = pd.read_csv(
        filepath_or_buffer=file_path,
        sep='\t',
    )
    return name, df


def load_all_tsv_files_from_path(
        path_to_dataset: str,
        n_jobs: int = -1
) -> Dict[str, pd.DataFrame]:
    """"
    :param path_to_dataset: the path to the .tsv file you want to load
    :param n_jobs: the number of jobs to run in parallel

    :return: a Dict[str, pd.DataFrame] with all the .tsv files loaded
    (the keys are the name of the files and the values are the loaded files as pd.DataFrames)
    """
    all_tsv_files = glob.glob(os.path.join(path_to_dataset, '*.tsv'))

    if n_jobs > 0:
        n_jobs = min(n_jobs, os.cpu_count())

    results = Parallel(n_jobs=n_jobs)(
        delayed(_load_one_tsv_file)(f) for f in tqdm(all_tsv_files, desc='Loading .tsv files')
    )
    dataframes: Dict[str, pd.DataFrame] = {name: df for name, df in results}

    return dataframes