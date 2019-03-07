from django import forms
from django.forms.models import inlineformset_factory

from .models import *

class AboxForm(forms.ModelForm):

    class Meta:
        model = a_box
        exclude=[]

AboxFormSet = inlineformset_factory(
    Project, a_box, form=AboxForm, extra=0
)

class AcircleForm(forms.ModelForm):

    class Meta:
        model = a_circle
        exclude=[]

AcircleFormSet = inlineformset_factory(
    Project, a_circle, form=AcircleForm, extra=0
)

class AconeForm(forms.ModelForm):

    class Meta:
        model = a_cone
        exclude=[]

AconeFormSet = inlineformset_factory(
    Project, a_cone, form=AconeForm, extra=0
)
