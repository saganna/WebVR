from django.urls import path
from django.contrib.auth import views as auth_views
from .views import *

urlpatterns = [
    path('account/', home, name='dashboard'),
    path('signup/', RegisterDoctor, name='doc_reg'),
    path('login/', DoctorLogin, name='doc_login'),
    path('logout/', logoutUser, name="doc_logout"),
    path('add-appointment/', addAppointment, name='add_appointment'),
    path('appointments/', AppointmentList, name='appointments'),
    path('patients/', PatientList, name='patients'),
    path('patients/<str:name>', PatientList, name='patient_history')



]
