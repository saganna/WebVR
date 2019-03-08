from django import forms
from django.forms.models import inlineformset_factory

from .models import *

class AboxForm(forms.ModelForm):

    class Meta:
        model = a_box
        exclude=[]

    def clean_position(self, *args, **kwargs):
        position = self.cleaned_data.get("position")
        t = position.split()

        if len(t)!=3:
            raise forms.ValidationError("Correct Form is '(value) (value) (value)'")
        return position

    def clean_rotation(self, *args, **kwargs):
        rotation = self.cleaned_data.get("rotation")
        t = rotation.split()

        if len(t)!=3:
            raise forms.ValidationError("Correct Form is '(value) (value) (value)'")
        return rotation

    def clean_scale(self, *args, **kwargs):
        scale = self.cleaned_data.get("scale")
        t = scale.split()

        if len(t)!=3:
            raise forms.ValidationError("Correct Form is '(value) (value) (value)'")
        return scale

AboxFormSet = inlineformset_factory(
    Project, a_box, form=AboxForm, extra=1
)

class AcircleForm(forms.ModelForm):

    class Meta:
        model = a_circle
        exclude=[]

    def clean_position(self, *args, **kwargs):
        position = self.cleaned_data.get("position")
        t = position.split()

        if len(t)!=3:
            raise forms.ValidationError("Correct Form is '(value) (value) (value)'")
        return position

    def clean_rotation(self, *args, **kwargs):
        rotation = self.cleaned_data.get("rotation")
        t = rotation.split()

        if len(t)!=3:
            raise forms.ValidationError("Correct Form is '(value) (value) (value)'")
        return rotation

    def clean_scale(self, *args, **kwargs):
        scale = self.cleaned_data.get("scale")
        t = scale.split()

        if len(t)!=3:
            raise forms.ValidationError("Correct Form is '(value) (value) (value)'")
        return scale

AcircleFormSet = inlineformset_factory(
    Project, a_circle, form=AcircleForm, extra=1
)

class AconeForm(forms.ModelForm):

    class Meta:
        model = a_cone
        exclude=[]

    def clean_position(self, *args, **kwargs):
        position = self.cleaned_data.get("position")
        t = position.split()

        if len(t)!=3:
            raise forms.ValidationError("Correct Form is '(value) (value) (value)'")
        return position

    def clean_rotation(self, *args, **kwargs):
        rotation = self.cleaned_data.get("rotation")
        t = rotation.split()

        if len(t)!=3:
            raise forms.ValidationError("Correct Form is '(value) (value) (value)'")
        return rotation

    def clean_scale(self, *args, **kwargs):
        scale = self.cleaned_data.get("scale")
        t = scale.split()

        if len(t)!=3:
            raise forms.ValidationError("Correct Form is '(value) (value) (value)'")
        return scale

AconeFormSet = inlineformset_factory(
    Project, a_cone, form=AconeForm, extra=1
)
