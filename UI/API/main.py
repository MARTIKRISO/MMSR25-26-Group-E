from fastapi import FastAPI, HTTPException
from contextlib import asynccontextmanager
from pathlib import Path
import pandas as pd
import tqdm
import json
from metrics import *

data_path = Path(__file__).parents[1] / "Data"

def load_all_csvs(root: Path) -> dict:
    cache = {}

    for path in tqdm.tqdm(root.rglob("*.parquet")):
        relative = path.relative_to(root)
        parts = relative.parts[:-1]  # directories
        filename = relative.name
        current = cache
        for part in parts:
            current = current.setdefault(part, {})
        current[filename] = pd.read_parquet(path, engine="pyarrow").sort_values("score", ascending = False)
    return cache
    
def load_data():
    tr = pd.read_csv(data_path / "tracks.csv")
    d = load_all_csvs(data_path)
    print("Loaded")
    return tr, d

def get_track_data(track_id: str): #-> id,artist,song,album_name,genre,url
    tracks = app.state.tracks.copy()
    tup = tracks[tracks["id"] == track_id].iloc[0]
    return tup

def get_track_id(song: str):
    tracks = app.state.tracks.copy()
    tup = tracks[tracks["song"] == song].iloc[0]
    return tup.id

@asynccontextmanager
async def lifespan(app: FastAPI):
    tracks, data = load_data()
    app.state.tracks = tracks
    app.state.data = data
    yield


def get_results(query, df):
    tracks = app.state.tracks
    query_track_id = get_track_id(query)
    df = df[df["id_1"] == query_track_id].iloc[1:]
    return df, query_track_id

def prettify_results(df):
    # Remove id_1, for each element of id_2, look up meta and add it
    df = df.drop(columns=["id_1"])
    metadata_fields = ["id", "artist", "song", "album_name", "genre", "url"]

    for field in metadata_fields:
        df[field] = df["id_2"].apply(lambda tid: get_track_data(tid)[field])
    
    df = df.drop(columns=["id_2"])
    return df

def calculate_metrics(query_id, retrieved_ids, k, songs_df):
    metrics = {
        "precision": round(precision_at_k(query_id, retrieved_ids, k, songs_df), 3),
        "ndcg": round(ndcg_at_k(query_id, retrieved_ids, k, songs_df), 3),
        "recall": round(recall_at_k(query_id, retrieved_ids, k, songs_df), 3),
        "f1": round(f1_at_k(query_id, retrieved_ids, k, songs_df), 3),
    }
    return metrics



app = FastAPI(lifespan=lifespan)


#WORKS WITH: late_fusion
@app.get("/tracks")
async def get_rank(query: str, track_cnt: int, sort_by: str, filter_by: str, algorithm: str, modalities: str, normalization: str):
    data = app.state.data
    try:
        if algorithm == "random":
            print("Running Random")
            tracks = app.state.tracks
            query_track_id = get_track_id(query)
            df = tracks.sample(frac=1)
            df["score"] = 1
            df.rename(columns={"id": "id_2"}, inplace=True)
            df["id_1"] = query_track_id
        elif algorithm in ["late_fusion", "early_fusion", "rrf", "nn"]:
            modals = sorted(modalities.split(r" "))
            print(f"Running {algorithm} with {modals}")
            if algorithm == "late_fusion":
                tt = data["multimodal"][algorithm][f"{normalization}_similarity_scores.parquet"].copy()
                df, query_track_id = get_results(query, tt)
            elif algorithm == "early_fusion":
                tt = data["multimodal"][algorithm][normalization][f"{'_'.join(modals)}_similarity_scores.parquet"].copy()
                df, query_track_id = get_results(query, tt)
            elif algorithm == "rrf":
                tt = data["multimodal"][algorithm][f"{normalization}_similarity_scores.parquet"].copy()
                tt.rename(columns={"query": "id_1", "target": "id_2"}, inplace=True)
                df, query_track_id = get_results(query, tt)
            elif algorithm == "nn":
                tt = data["nn"]["max_scores"][f"{'_'.join(modals)}_max_scores.parquet"].copy()
                df, query_track_id = get_results(query, tt)

        else:
            print(f"Running Unimodal with {modalities}")
            #unimodal
            tt = data["unimodal"][normalization][f"{modalities}_similarity_scores.parquet"].copy()
            df, query_track_id = get_results(query, tt)

        #Filter by author, common genre

        if filter_by == "artist":
            query_artist = get_track_data(query_track_id).artist
            df = df[df["id_2"].apply(lambda tid: get_track_data(tid).artist == query_artist)]
        elif filter_by == "genre":
            query_genres = get_track_data(query_track_id).genre
            df = df[df["id_2"].apply(lambda tid: len(set(get_track_data(tid).genre).intersection(query_genres)) > 0)]

        #Resort by alpha order(songname, artist), duration

        def sort_dataframe(df, field, ascending=False):
            sort_col = f"_sort_{field}"
            df[sort_col] = df["id_2"].apply(lambda tid: get_track_data(tid)[field])
            return df.sort_values(by=sort_col, ascending=ascending).drop(columns=[c for c in df.columns if c.startswith("_sort_")])
        
        if sort_by in ["song", "artist"]:
            df = sort_dataframe(df, sort_by)

        #Truncate df by track_cnt
        df = df[:track_cnt]

        metrics = calculate_metrics(query_track_id, df["id_2"].tolist(), track_cnt, app.state.tracks)

        df = prettify_results(df)

        return [df.to_dict(orient="records"), metrics]
    except Exception as e:
        print(e)