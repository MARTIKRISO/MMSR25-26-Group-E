from pathlib import Path

class MMSRService:
    def __init__(self, path_to_parquet_files: str):
        self.ALGORITHMS = ["random"] #TODO: Load them from the parquet files
        self.GENRES = ["rock", "pop", "jazz"] #TODO: Load them from the parquet files
        self.SORT_OPTIONS = ["title", "artist", "duration"]
    
    @staticmethod
    def generate_tracks(query: str, track_cnt: int, sort_by: str, filter_by: str, algorithm: str) -> list[dict[str, str]]:
    
        if algorithm == "sample":
            track = {
                "title": "Sample Track",
                "artist": "Sample Artist",
                "album": "Sample Album",
                "genre": "Sample Genre",
                "duration": "3:45"
            }
            return [track] * track_cnt
        else:
            return []  # TODO: Implement other algorithms
        
    @staticmethod
    def get_project_path() -> str:
        return str(Path(__file__).parents[3])
    