from flask import Flask, render_template, request
from services import MMSRService

app = Flask(__name__)

@app.route("/")
def index():
    query      = request.args.get("query") or ""
    track_cnt  = request.args.get("track_count") or "10"
    
    sort_by    = request.args.get("sort_by") or "relevance"
    filter_by  = request.args.get("filter_by") or "none"
    algorithm  = request.args.get("algorithm") or "random"
    modalities = request.args.get("modalities") or ""
    normalization = request.args.get("normalization") or "raw"

    try:
        track_cnt = int(track_cnt)
    except ValueError:
        track_cnt = 10

    
    metrics = {
        "Precision": "N/A",
        "Recall": "N/A",
        "F1-Score": "N/A",
        "NDCG": "N/A"
    }
    results = []
    api = MMSRService()
    if query != "":
        results, metrics = api.generate_tracks(
            query= query,
            track_cnt= track_cnt,
            sort_by= sort_by,
            filter_by= filter_by,
            algorithm= algorithm,
            modalities= modalities,
            normalization= normalization
        )
    algorithm_labels = {
        "random": "Random Baseline",
        "unimodal": "Unimodal",
        "early_fusion": "Early Fusion",
        "late_fusion": "Late Fusion",
        "rrf": "Late Fusion (RRF)",
        "nn": "Neural Network"
    }
    normalization_labels = {
        "raw": "Raw (no normalization)",
        "max_abs": "Max-Abs",
        "min_max": "Min-Max",
        "standard": "Standard",
        "robust": "Robust"
    }

    context = {
        "query": query,
        "track_count": track_cnt,
        "sort_by": sort_by,
        "filter_by": filter_by,
        "algorithm": algorithm,
        "modalities": modalities,
        "normalization": normalization,
        "results": results,
        "metrics": metrics,
        "algorithm_label": algorithm_labels.get(algorithm, algorithm.replace('_', ' ').title()),
        "normalization_label": normalization_labels.get(normalization, normalization.replace('_', ' ').title())
    }

    return render_template("index.html", **context)

@app.route("/test")
def get_yt_video_id(url):
    """Helper to extract YouTube video ID from various URL formats"""
    if not url:
        return ""
    if "watch?v=" in url:
        return url.split("watch?v=")[1].split("&")[0]
    elif "youtu.be/" in url:
        return url.split("youtu.be/")[1].split("?")[0]
    elif "embed/" in url:
        return url.split("embed/")[1].split("?")[0]
    return ""

def youtube_thumbnail(url):
    """Return the high-quality thumbnail URL for a YouTube video"""
    video_id = get_yt_video_id(url)
    if video_id:
        return f"https://img.youtube.com/vi/{video_id}/mqdefault.jpg"
    return ""

def youtube_watch_url(url):
    """Convert any YouTube URL format to a standard watch URL"""
    video_id = get_yt_video_id(url)
    if video_id:
        return f"https://www.youtube.com/watch?v={video_id}"
    return url

app.jinja_env.filters['youtube_thumbnail'] = youtube_thumbnail
app.jinja_env.filters['youtube_watch_url'] = youtube_watch_url

if __name__ == "__main__":
    app.run(debug=True, port=5000)
