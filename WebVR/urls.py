from django.urls import path
from . import views

urlpatterns = [
    path('', views.myproject, name='myprojects'),
    path('createVR/', views.createVR, name='creating VR'),
]