import re
from django.shortcuts import render
from django.conf.urls.static import static
from django.http import HttpResponse

def index(request):
    query      = request.GET.get("query") or ""
    track_cnt  = request.GET.get("track_count") or "10"

    try:
        track_cnt = int(track_cnt)
    except ValueError:
        track_cnt = 10

    # TODO: search logic
    results = []
    if query:
        pass # return tracks to results
    
    context = {
        "query": query,
        "track_count": track_cnt,
        "results": results,
    }

    return render(request, "MMSR_WebUI/index.html", context)