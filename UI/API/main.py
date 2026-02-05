"""
FastAPI backend for the MMSR Music Search System.
Handles track search requests with various algorithms, modalities, and normalization.
"""

import gc
from contextlib import asynccontextmanager
from pathlib import Path
from typing import Optional

import pandas as pd
import tqdm
from fastapi import FastAPI

from metrics import (
    precision_at_k,
    recall_at_k,
    f1_at_k,
    ndcg_at_k,
)


# =============================================================================
# Configuration
# =============================================================================

DATA_PATH = Path(__file__).parents[1] / "Data"


# =============================================================================
# Data Loading
# =============================================================================

def index_all_parquets(root: Path) -> dict:
    """
    Build a nested dict mirroring the directory structure.
    
    Leaf values are Path objects to parquet files for lazy loading.
    
    Args:
        root: Root directory to search for parquet files
        
    Returns:
        Nested dictionary with parquet file paths
    """
    index = {}
    
    for path in tqdm.tqdm(root.rglob("*.parquet")):
        relative = path.relative_to(root)
        parts = relative.parts[:-1]  # directories
        filename = relative.name

        current = index
        for part in parts:
            current = current.setdefault(part, {})
        current[filename] = path

    return index


def load_parquet_df(path: Path, *, sort_by_score: bool = True) -> pd.DataFrame:
    """
    Load a parquet file and optionally sort by score.
    
    Args:
        path: Path to parquet file
        sort_by_score: Whether to sort by 'score' column descending
        
    Returns:
        Loaded DataFrame
    """
    df = pd.read_parquet(path, engine="pyarrow")
    
    if sort_by_score and "score" in df.columns:
        df = df.sort_values("score", ascending=False)
    
    return df


def load_data() -> tuple[pd.DataFrame, dict]:
    """
    Load tracks CSV and index all parquet files.
    
    Returns:
        Tuple of (tracks DataFrame, parquet file index)
    """
    tracks = pd.read_csv(DATA_PATH / "tracks.csv")
    parquet_index = index_all_parquets(DATA_PATH)
    print("Indexed parquet files (lazy loading enabled)")
    
    return tracks, parquet_index


# =============================================================================
# Track Utilities
# =============================================================================

def get_track_data(track_id: str) -> pd.Series:
    """Get track metadata by ID."""
    tracks = app.state.tracks
    return tracks.loc[tracks["id"] == track_id].iloc[0]


def get_track_id(song: str) -> str:
    """Get track ID by song name."""
    tracks = app.state.tracks
    return tracks.loc[tracks["song"] == song].iloc[0].id


def get_results(query: str, df: pd.DataFrame) -> tuple[pd.DataFrame, str]:
    """
    Filter results for a given query.
    
    Args:
        query: Song name to search for
        df: DataFrame with similarity scores
        
    Returns:
        Tuple of (filtered DataFrame, query track ID)
    """
    query_track_id = get_track_id(query)
    df = df[df["id_1"] == query_track_id].iloc[1:]
    return df, query_track_id


def prettify_results(df: pd.DataFrame) -> pd.DataFrame:
    """
    Add human-readable metadata to results.
    
    Args:
        df: DataFrame with track IDs
        
    Returns:
        DataFrame with added metadata fields
    """
    df = df.drop(columns=["id_1"])
    metadata_fields = ["id", "artist", "song", "album_name", "genre", "url"]

    for field in metadata_fields:
        df[field] = df["id_2"].apply(lambda tid: get_track_data(tid)[field])

    df = df.drop(columns=["id_2"])
    return df


# =============================================================================
# Metrics Calculation
# =============================================================================

def calculate_metrics(
    query_id: str,
    retrieved_ids: list,
    k: int,
    songs_df: pd.DataFrame
) -> dict:
    """
    Calculate search quality metrics.
    
    Args:
        query_id: ID of the query track
        retrieved_ids: List of retrieved track IDs
        k: Number of results to consider
        songs_df: DataFrame with all songs
        
    Returns:
        Dictionary with precision, recall, f1, and ndcg scores
    """
    return {
        "precision": round(precision_at_k(query_id, retrieved_ids, k, songs_df), 3),
        "recall": round(recall_at_k(query_id, retrieved_ids, k, songs_df), 3),
        "f1": round(f1_at_k(query_id, retrieved_ids, k, songs_df), 3),
        "ndcg": round(ndcg_at_k(query_id, retrieved_ids, k, songs_df), 3),
    }


# =============================================================================
# FastAPI Application
# =============================================================================

@asynccontextmanager
async def lifespan(app: FastAPI):
    """Application lifespan manager for loading data on startup."""
    tracks, parquet_index = load_data()
    app.state.tracks = tracks
    app.state.data = parquet_index
    yield
    # No explicit cleanup needed - we don't hold large DataFrames globally


app = FastAPI(lifespan=lifespan)


# =============================================================================
# API Endpoints
# =============================================================================

@app.get("/tracks")
async def get_tracks(
    query: str,
    track_cnt: int,
    sort_by: str,
    filter_by: str,
    algorithm: str,
    modalities: str,
    normalization: str
):
    """
    Search for similar tracks.
    
    Args:
        query: Song name to search similar tracks for
        track_cnt: Number of tracks to return
        sort_by: Field to sort results by ('song', 'artist', or 'score')
        filter_by: Filter criteria ('artist', 'genre', or 'none')
        algorithm: Search algorithm ('random', 'unimodal', 'early_fusion', 
                   'late_fusion', 'rrf', 'nn')
        modalities: Space-separated modalities ('lyrics', 'audio', 'video')
        normalization: Normalization method ('raw', 'max_abs', 'min_max', 
                       'standard', 'robust')
    
    Returns:
        List containing [results_list, metrics_dict]
    """
    data = app.state.data
    tt = None
    df = None

    try:
        df, query_track_id = _execute_search(query, algorithm, modalities, normalization, data)
        df = _apply_filters(df, query_track_id, filter_by)
        df = df[:track_cnt]
        df = _apply_sorting(df, sort_by)
        
        metrics = calculate_metrics(
            query_track_id,
            df["id_2"].tolist(),
            track_cnt,
            app.state.tracks
        )
        
        df = prettify_results(df)
        return [df.to_dict(orient="records"), metrics]

    finally:
        # Drop references to large DataFrames for memory efficiency
        del tt
        del df
        gc.collect()


# =============================================================================
# Search Algorithm Handlers
# =============================================================================

def _execute_search(
    query: str,
    algorithm: str,
    modalities: str,
    normalization: str,
    data: dict
) -> tuple[pd.DataFrame, str]:
    """
    Execute the appropriate search algorithm.
    
    Returns:
        Tuple of (results DataFrame, query track ID)
    """
    if algorithm == "random":
        return _search_random(query)
    
    if algorithm in ["late_fusion", "early_fusion", "rrf", "nn"]:
        return _search_multimodal(query, algorithm, modalities, normalization, data)
    
    # Default: unimodal search
    return _search_unimodal(query, modalities, normalization, data)


def _search_random(query: str) -> tuple[pd.DataFrame, str]:
    """Perform random baseline search."""
    print("Running Random")
    
    tracks = app.state.tracks
    query_track_id = get_track_id(query)
    
    df = tracks.sample(frac=1)
    df["score"] = 1
    df.rename(columns={"id": "id_2"}, inplace=True)
    df["id_1"] = query_track_id
    
    return df, query_track_id


def _search_unimodal(
    query: str,
    modalities: str,
    normalization: str,
    data: dict
) -> tuple[pd.DataFrame, str]:
    """Perform unimodal search."""
    print(f"Running Unimodal with {modalities}")
    
    path = data["unimodal"][normalization][f"{modalities}_similarity_scores.parquet"]
    tt = load_parquet_df(path, sort_by_score=True)
    
    return get_results(query, tt)


def _search_multimodal(
    query: str,
    algorithm: str,
    modalities: str,
    normalization: str,
    data: dict
) -> tuple[pd.DataFrame, str]:
    """Perform multimodal fusion search."""
    modals = sorted(modalities.split(" "))
    print(f"Running {algorithm} with {modals}")

    if algorithm == "late_fusion":
        path = data["multimodal"][algorithm][f"{normalization}_similarity_scores.parquet"]
        tt = load_parquet_df(path, sort_by_score=True)
        return get_results(query, tt)

    if algorithm == "early_fusion":
        path = data["multimodal"][algorithm][normalization][
            f"{'_'.join(modals)}_similarity_scores.parquet"
        ]
        tt = load_parquet_df(path, sort_by_score=True)
        return get_results(query, tt)

    if algorithm == "rrf":
        path = data["multimodal"][algorithm][f"{normalization}_similarity_scores.parquet"]
        tt = load_parquet_df(path, sort_by_score=True)
        tt.rename(columns={"query": "id_1", "target": "id_2"}, inplace=True)
        return get_results(query, tt)

    if algorithm == "nn":
        path = data["nn"]["max_scores"][f"{'_'.join(modals)}_max_scores.parquet"]
        tt = load_parquet_df(path, sort_by_score=True)
        return get_results(query, tt)

    raise ValueError(f"Unknown algorithm: {algorithm}")


# =============================================================================
# Result Processing
# =============================================================================

def _apply_filters(
    df: pd.DataFrame,
    query_track_id: str,
    filter_by: str
) -> pd.DataFrame:
    """Apply filtering based on artist or genre."""
    if filter_by == "artist":
        query_artist = get_track_data(query_track_id).artist
        df = df[df["id_2"].apply(
            lambda tid: get_track_data(tid).artist == query_artist
        )]
    
    elif filter_by == "genre":
        query_genres = get_track_data(query_track_id).genre
        df = df[df["id_2"].apply(
            lambda tid: len(
                set(get_track_data(tid).genre).intersection(query_genres)
            ) > 0
        )]
    
    return df


def _apply_sorting(df: pd.DataFrame, sort_by: str) -> pd.DataFrame:
    """Apply sorting by song or artist field."""
    if sort_by not in ["song", "artist"]:
        return df
    
    sort_col = f"_sort_{sort_by}"
    df[sort_col] = df["id_2"].apply(lambda tid: get_track_data(tid)[sort_by])
    
    return (
        df.sort_values(by=sort_col, ascending=True)
          .drop(columns=[c for c in df.columns if c.startswith("_sort_")])
    )