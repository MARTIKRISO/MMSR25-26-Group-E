from pathlib import Path
import pandas as pd
import ast
import sqlite3

data_path = Path(__file__).parent / "Dataset"


class Preprocessing():
    def __init__(self):
        self.curr_path = Path(__file__).parent
        self.root = Path(__file__).parents[2]
        #self.data_path = self.root / "Dataset"
        self.id_information = pd.read_csv(self.root / "Dataset" / "id_information_mmsr.tsv", sep="\t")
        self.id_genres = pd.read_csv(self.root / "Dataset" / "id_genres_mmsr.tsv", sep="\t")
        self.id_url = pd.read_csv(self.root / "Dataset" / "id_url_mmsr.tsv", sep="\t")
    
    def merge_dfs(self) -> None:
        # check if "merged_track_info.csv" exists
        if (self.curr_path / "merged_track_info.csv").exists():
            self.merged_df = pd.read_csv(self.curr_path / "merged_track_info.csv")
            return
        
        # Merge df1 and df2 on 'id'
        merged_df = pd.merge(self.id_information, self.id_genres, on='id', how='left')

        # Merge the result with df3 on 'id'
        merged_df = pd.merge(merged_df, self.id_url, on='id', how='left')
        
        self.merged_df = merged_df
    
    def export_merged_df_csv(self, filename: str = "merged_track_info.csv"):
        if not hasattr(self, 'merged_df'):
            self.merge_dfs()
        self.merged_df.to_csv(self.curr_path / filename, index=False)
        
    def export_to_db(self):
        df = self.merged_df.copy()
        
        df['genre'] = df['genre'].apply(lambda x: ast.literal_eval(x) if pd.notnull(x) else [])

        # Get unique genres
        all_genres = sorted({g for sublist in df['genre'] for g in sublist})

        # Add boolean columns for each genre
        for genre in all_genres:
            df[genre] = df['genre'].apply(lambda genres: genre in genres)

        # Drop original genre column
        df = df.drop(columns=['genre'])

        # Connect to SQLite (creates file if it doesn't exist)
        conn = sqlite3.connect("music.db")

        # Save DataFrame to SQLite table named 'songs'
        df.to_sql('songs', conn, if_exists='replace', index=False)

        # Close connection
        conn.close()
        
if __name__ == "__main__":
    prep = Preprocessing()
    prep.merge_dfs()
    prep.export_to_db()