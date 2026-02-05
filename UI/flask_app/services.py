"""
MMSR Service module for handling music search functionality.
Provides track search, autocomplete, and API communication.
"""

import ast
import os

import pandas as pd
import requests


class MMSRService:
    """Service class for MMSR music search operations."""
    
    API_PORT = 69
    API_URL = f"http://localhost:{API_PORT}/tracks"
    
    ERROR_RESPONSE = [{
        "song": "ERROR: Bad query or something else went wrong",
        "artist": "",
        "genre": "",
        "score": ""
    }]
    
    INDEX_RESPONSE = [{
        "song": "Enter a track to get started!",
        "artist": "",
        "genre": "",
        "score": ""
    }]
    
    DEFAULT_METRICS = {
        "Precision": "N/A",
        "Recall": "N/A",
        "F1-Score": "N/A",
        "NDCG": "N/A"
    }

    def __init__(self):
        """Initialize the service and load track data."""
        self.tracks_df = None
        self._load_tracks()

    def _load_tracks(self):
        """Load tracks from CSV file for autocomplete functionality."""
        try:
            csv_path = os.path.join(
                os.path.dirname(__file__), '..', 'Data', 'tracks.csv'
            )
            self.tracks_df = pd.read_csv(csv_path)
        except Exception as e:
            print(f"Error loading tracks CSV: {e}")
            self.tracks_df = pd.DataFrame()

    def autocomplete_songs(self, query, limit=15):
        """
        Search for songs matching the query string.
        
        Args:
            query: Search string to match against song names and artists
            limit: Maximum number of results to return (default: 15)
            
        Returns:
            List of dictionaries containing matching song data
        """
        if self.tracks_df is None or self.tracks_df.empty or not query:
            return []
        
        query_lower = query.lower()
        
        # Search in song name and artist columns
        mask = (
            self.tracks_df['song'].str.lower().str.contains(query_lower, na=False) |
            self.tracks_df['artist'].str.lower().str.contains(query_lower, na=False)
        )
        matches = self.tracks_df[mask].head(limit)
        
        # Convert to list of dictionaries
        results = []
        for _, row in matches.iterrows():
            results.append({
                'id': row['id'],
                'song': row['song'],
                'artist': row['artist'],
                'album': row.get('album_name', ''),
                'genre': row.get('genre', ''),
                'url': row.get('url', '')
            })
        
        return results

    def generate_tracks(self, query, track_cnt, sort_by, filter_by, 
                        algorithm, modalities, normalization):
        """
        Generate track search results from the backend API.
        
        Args:
            query: Search query string
            track_cnt: Number of tracks to return
            sort_by: Sort order for results
            filter_by: Filter criteria
            algorithm: Search algorithm to use
            modalities: Search modalities
            normalization: Normalization method
            
        Returns:
            Tuple of (results_list, metrics_dict)
        """
        print(f"Query: {query}, Tracks: {track_cnt}, Algorithm: {algorithm}")
        
        if not query:
            return self.INDEX_RESPONSE, self.DEFAULT_METRICS.copy()
        
        try:
            response = requests.get(
                self.API_URL,
                params={
                    "query": query,
                    "track_cnt": track_cnt,
                    "sort_by": sort_by,
                    "filter_by": filter_by,
                    "algorithm": algorithm,
                    "modalities": modalities,
                    "normalization": normalization
                }
            )
            
            data = response.json()
            
            if isinstance(data, list) and len(data) == 2:
                results, metrics = data
                
                # Process each result item
                for item in results:
                    item["genre"] = ", ".join(ast.literal_eval(item["genre"]))
                    item["score"] = float(item["score"])
                
                return results, metrics
            
            return self.ERROR_RESPONSE, self.DEFAULT_METRICS.copy()
            
        except (requests.RequestException, ValueError, TypeError) as e:
            print(f"Service error: {e}")
            return self.ERROR_RESPONSE, self.DEFAULT_METRICS.copy()
