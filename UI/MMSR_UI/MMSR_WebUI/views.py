from django.shortcuts import render
from django.conf.urls.static import static
from django.http import HttpResponse

def index(request):
    return render(request, "MMSR_WebUI/index.html")