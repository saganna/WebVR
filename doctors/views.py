from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, get_user,login, logout
from django.contrib.auth.decorators import login_required
from datetime import datetime, date, timedelta
from django.contrib import messages
from django.utils import timezone
from django.core.paginator import Paginator
from datetime import datetime
from .models import *
from .forms import *
from .filters import *
from users.models import Profile, User

# Create your views here.
@login_required(login_url='doc_login')
def home(request):
    current_user = request.user
    print(current_user.id)
    total_app = Appointment.objects.filter().count()
    app_today = Appointment.objects.filter(date_of_appointment__gte=timezone.now().replace(
        hour=0, minute=0, second=0), date_of_appointment__lte=timezone.now().replace(hour=23, minute=59, second=59)).count()
    context = {
        'app_today':app_today,
        'total_app':total_app
    }
    return render(request, 'doctors/index.html', context)


def RegisterDoctor(request):
    if request.method == 'POST':
        form = DoctorRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! You are now able to log in')
            return redirect('doc_login')
    else:
        form = DoctorRegisterForm()
    return render(request, 'doctors/register.html', {'form':form})

def DoctorLogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.info(request, 'Incorrect Username or Password!')
    context = {}
    return render(request, 'doctors/login.html', context)

# logout
def logoutUser(request):
    logout(request)
    return redirect('doc_login')


def AppointmentList(request):
    appointments = Appointment.objects.all().order_by('-date_of_appointment')
    myFilter = AppointmentFilter(request.GET, queryset=appointments)
    appointments = myFilter.qs
    paginator = Paginator(appointments, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'appointments': appointments,
               'page_obj': page_obj, 'myFilter': myFilter}
    return render(request, 'doctors/appointment_list.html', context)

def addAppointment(request):
    form = AppointmentForm()
    clients = User.objects.all()
    myFilter = AppointmentFilter(request.GET, queryset=clients)
    if request.method == 'POST':
        user = get_user(request)
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    context = {'form': form, 'myFilter': myFilter}
    return render(request, 'doctors/add_appointment.html', context)


def PatientList(request):
    patient = Profile.objects.all().order_by('-id')
    paginator = Paginator(patient, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'patient': patient, 'page_obj': page_obj, }

    return render(request, 'doctors/patient.html', context)
    

def PatientHistory(request, name):
    patient = Profile.objects.get(name=name)
    appointment = Appointment.objects.filter(client_by=patient).order_by('-date_of_appoitnment')
    myFilter = AppointmentFilter(request.GET, queryset=appointment)
    appointment = myFilter.qs
    paginator = Paginator(appointment, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    

    context = {'appointment': appointment, ' patient': patient, 
               'page_obj': page_obj, 'myFilter': myFilter}
    return render(request, 'doctor/patient_history.html', context)