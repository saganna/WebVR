from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('', views.Home, name='home'),
    path('home/', views.Home, name='Home'),
    path('createVR/', ProjectCreateView.as_view(), name='createVR'),
    path('updateVR/<int:pk>/', ProjectUpdateView.as_view(), name='updateVR'),
    path('deleteVR/<int:pk>/', ProjectDeleteView.as_view(), name='deleteVR'),
    path('projects/', ProjectListView.as_view(), name='project-home'),
    path('projects/<str:username>', UserProjectListView.as_view(), name='user-projects'),
    path('projects/<int:pk>/', views.showproject_view, name='show project'),
]
