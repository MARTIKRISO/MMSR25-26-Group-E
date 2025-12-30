from django.shortcuts import render
from django.http import HttpResponse

from MMSR_WebUI.services import MMSRService

def index(request):
    query      = request.GET.get("query") or ""
    track_cnt  = request.GET.get("track_count") or "10"
    
    sort_by    = request.GET.get("sort_by") or "relevance"
    filter_by  = request.GET.get("filter_by") or "none"
    algorithm  = request.GET.get("algorithm") or "default"
    modalitiesInput = request.GET.get("modalitiesInput")
    normalizationInput = request.GET.get("normalizationInput") or "raw"

    try:
        track_cnt = int(track_cnt)
    except ValueError:
        track_cnt = 10

    results = MMSRService.generate_tracks(
        query=query,
        track_cnt=track_cnt,
        sort_by=sort_by,
        filter_by=filter_by,
        algorithm="sample"  # TODO: Replace with actual algorithm variable
    )

    context = {
        "query": query,
        "track_count": track_cnt,
        "sort_by": sort_by,
        "filter_by": filter_by,
        "algorithm": algorithm,
        "results": results,
    }

    return render(request, "MMSR_WebUI/index.html", context)

def test(request):
    return HttpResponse(MMSRService.get_curr_path())