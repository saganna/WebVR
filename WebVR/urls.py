from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('', views.Home, name='home'),
    path('home/', views.Home, name='Home'),
    path('createVR/', ProjectCreateView.as_view(), name='createVR'),
    path('projects/', ProjectListView.as_view(), name='project-home'),
    path('projects/', ProjectListView.as_view(), name='project-home'),
    path('projects/<int:id>/', views.showProject_view, name='show Project'),
    path('projects/<str:name>/', views.showproject_view, name='show project'),
]
