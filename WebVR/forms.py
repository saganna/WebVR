from django import forms

from .models import *

class ProjectCreateForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = [
            'name',
            'description',
            'changed_date',
        ]
