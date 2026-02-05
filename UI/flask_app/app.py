"""
Flask application for the MMSR Music Search System.
Provides web interface and API endpoints for searching and autocompleting songs.
"""

from flask import Flask, render_template, request, jsonify
from services import MMSRService

app = Flask(__name__)
mmsr_service = MMSRService()


# =============================================================================
# Label Mappings
# =============================================================================

ALGORITHM_LABELS = {
    "random": "Random Baseline",
    "unimodal": "Unimodal",
    "early_fusion": "Early Fusion",
    "late_fusion": "Late Fusion",
    "rrf": "Late Fusion (RRF)",
    "nn": "Neural Network"
}

NORMALIZATION_LABELS = {
    "raw": "Raw (no normalization)",
    "max_abs": "Max-Abs",
    "min_max": "Min-Max",
    "standard": "Standard",
    "robust": "Robust"
}

DEFAULT_METRICS = {
    "Precision": "N/A",
    "Recall": "N/A",
    "F1-Score": "N/A",
    "NDCG": "N/A"
}


# =============================================================================
# Routes
# =============================================================================

@app.route("/")
def index():
    """Main page route - handles search queries and displays results."""
    # Parse request parameters
    query = request.args.get("query", "")
    track_cnt = request.args.get("track_count", "10")
    sort_by = request.args.get("sort_by", "relevance")
    filter_by = request.args.get("filter_by", "none")
    algorithm = request.args.get("algorithm", "random")
    modalities = request.args.get("modalities", "")
    normalization = request.args.get("normalization", "raw")

    # Validate track count
    try:
        track_cnt = int(track_cnt)
    except ValueError:
        track_cnt = 10

    # Get search results if query provided
    metrics = DEFAULT_METRICS.copy()
    results = []
    
    if query:
        results, metrics = mmsr_service.generate_tracks(
            query=query,
            track_cnt=track_cnt,
            sort_by=sort_by,
            filter_by=filter_by,
            algorithm=algorithm,
            modalities=modalities,
            normalization=normalization
        )

    # Build template context
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
        "algorithm_label": ALGORITHM_LABELS.get(
            algorithm, algorithm.replace('_', ' ').title()
        ),
        "normalization_label": NORMALIZATION_LABELS.get(
            normalization, normalization.replace('_', ' ').title()
        )
    }

    return render_template("index.html", **context)


@app.route("/api/autocomplete")
def autocomplete():
    """API endpoint for song autocomplete suggestions."""
    query = request.args.get("q", "")
    
    if len(query) < 2:
        return jsonify([])
    
    results = mmsr_service.autocomplete_songs(query, limit=15)
    return jsonify(results)


# =============================================================================
# YouTube URL Helpers
# =============================================================================

def get_yt_video_id(url):
    """Extract YouTube video ID from various URL formats."""
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
    """Return the high-quality thumbnail URL for a YouTube video."""
    video_id = get_yt_video_id(url)
    if video_id:
        return f"https://img.youtube.com/vi/{video_id}/mqdefault.jpg"
    return ""


def youtube_watch_url(url):
    """Convert any YouTube URL format to a standard watch URL."""
    video_id = get_yt_video_id(url)
    if video_id:
        return f"https://www.youtube.com/watch?v={video_id}"
    return url


# Register Jinja2 template filters
app.jinja_env.filters['youtube_thumbnail'] = youtube_thumbnail
app.jinja_env.filters['youtube_watch_url'] = youtube_watch_url


# =============================================================================
# Application Entry Point
# =============================================================================

if __name__ == "__main__":
    app.run(debug=True, port=5000)
