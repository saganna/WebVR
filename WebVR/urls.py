from django.urls import path
from . import views

urlpatterns = [
    path('', views.myproject, name='myprojects'),
    path('createVR/', views.CreateVR_view, name='creating VR'),
    path('projects/<int:id>/', views.showProject_view, name='show Project'),
    path('projects/<str:name>/', views.showproject_view, name='show project'),
]
