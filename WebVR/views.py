from django.shortcuts import render

from django.http import HttpResponse
from .models import *

# Create your views here.
def index(request):
    return HttpResponse("hihi")

def Home_view(request):
    return HttpResponse("This is a homepage")

def myproject(request):
    project_list = project.objects
    output ='\n'.join(p.name for p in project_list)
    return HttpResponse(output)

def createVR(request):
    template_name='WebVR/createVR.html'
    return render(request, template_name, {})