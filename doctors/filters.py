from django.db.models import fields
import django_filters
from django_filters import CharFilter, NumberFilter, DateFilter
from .models import *

class AppointmentFilter(django_filters.FilterSet):
    name = CharFilter(lookup_expr='icontains', label='Name')
    class Meta:
        model = Appointment
        fields = ['client']