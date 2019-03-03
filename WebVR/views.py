from django.shortcuts import render

from django.http import HttpResponse
from .models import *
from .forms import *

# Create your views here.
def index(request):
    return HttpResponse("hihi")

def Home_view(request):
    template='WebVR/Home.html'
    return render(request, template, {})

def myproject(request):
    project_list = project.objects
    output ='\n'.join(p.name for p in project_list)
    return HttpResponse(output)

def CreateVR_view(request):
    form = ProjectCreateForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProjectCreateForm()

    context = {
        'form' : form
    }
    template='WebVR/createVR.html'
    return render(request, template, context)

def showProject_view(request, id):
    obj = Project.objects.get(id=id)
    context={
        "object" : obj
    }
    print(obj.a_box_set.all()[0].pos())
    return render(request, "WebVR/showproject.html", context)

def showproject_view(request, name):
    obj = Project.objects.get(name=name)
    context={
        "object" : obj
    }
    return render(request, "WebVR/showproject.html", context)
