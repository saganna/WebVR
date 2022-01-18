from re import I
from django.contrib.auth import login
from django.shortcuts import render, get_object_or_404
from django.test import client
from django.views.generic import *

from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.db import transaction
from django.contrib.auth.decorators import login_required

from users.models import Profile
from .models import *
from .forms import *
from doctors.models import *
from django.core.paginator import Paginator

# Create your views here.
@login_required(login_url='login')
def Home(request):
    template='WebVR/Home.html'
    user = request.user
    client = User.objects.get(username=user)
    print(client)
    appointments = Appointment.objects.filter(client=client)
    context = {'appointments': appointments,}
    return render(request, template, context)



