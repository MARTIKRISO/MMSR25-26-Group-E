from pathlib import Path
import requests as r
import ast

class MMSRService:
    def __init__(self, API_port = 69):
        self.API_port = 69
        self.url = f"http://localhost:{self.API_port}/tracks"
        self.error_resp = [{"song": "ERROR: Bad query or something else went wrong", "artist":"", "genre": "", "score": ""}]
        self.index_resp = [{"song": "Enter a track to get started!", "artist":"", "genre": "", "score": ""}]
    
    def generate_tracks(self, query, track_cnt, sort_by, filter_by, algorithm, modalities, normalization):
        print(query, track_cnt, sort_by, filter_by, algorithm, modalities, normalization)
        
        default_metrics = {"Precision": "N/A", "Recall": "N/A", "F1-Score": "N/A", "NDCG": "N/A"}
        
        if query == "":
            return self.index_resp, default_metrics
            
        try:
            res = r.get(self.url, params={"query": query, "track_cnt": track_cnt, "sort_by": sort_by, "filter_by": filter_by, "algorithm": algorithm,
                                    "modalities": modalities, "normalization": normalization})
            
            data = res.json()
            if isinstance(data, list) and len(data) == 2:
                res_list, metrics = data
                for item in res_list:
                    item["genre"] = ", ".join(ast.literal_eval(item["genre"]))
                    item["score"] = float(item["score"])
                return res_list, metrics
            else:
                return self.error_resp, default_metrics
                
        except (r.RequestException, ValueError, TypeError) as e:
            print(f"Service error: {e}")
            return self.error_resp, default_metrics
