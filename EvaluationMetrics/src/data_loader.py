import sqlite3
import pandas as pd

def load_songs_data(db_path='Dataset/music.db'):
    """columns:id, artist, song, album name, url, genre columns (0 or 1 for each) """

    conn = sqlite3.connect(db_path)
    df = pd.read_sql_query('SELECT * FROM songs', conn)
    conn.close()

    return df

def get_genre_columns():
    """get list of all genre column names"""

    # All columns except the first 5 (id, artist, song, album name, url)
    conn = sqlite3.connect('Dataset/music.db')
    cursor = conn.cursor()
    cursor.execute('PRAGMA table_info(songs)')
    all_columns = [col[1] for col in cursor.fetchall()]
    conn.close()
    
    # genre start from index 5
    genre_columns = all_columns[5:]
    
    return genre_columns

def get_genres_for_track(track_id, songs_df, genre_columns):
    track_row = songs_df[songs_df['id'] == track_id]
    
    if track_row.empty:
        return set()
    
    track_genres = track_row[genre_columns].iloc[0]
    active_genres = set(track_genres[track_genres == 1].index.tolist())
    
    return active_genres

if __name__ == "__main__":
    # test the functions
    print("load data...")
    df = load_songs_data()
    print(f"{len(df)} songs")
    
    genres = get_genre_columns()
    print(f"{len(genres)} genre columns")
    
    # test with n track
    first_track_id = df.iloc[5]['id']
    first_track_genres = get_genres_for_track(first_track_id, df, genres)
    print(f"\nfirst track ({first_track_id}) genres: {first_track_genres}")
