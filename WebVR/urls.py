from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('', views.Home, name='home'),
    path('home/', views.Home, name='Home'),

]
