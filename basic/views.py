from django.shortcuts import render

# Create your views here.

def Index(request):
    template='WebVR/index.html'
    return render(request, template, {})
