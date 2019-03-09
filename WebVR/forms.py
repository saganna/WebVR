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

class AcylinderForm(forms.ModelForm):

    class Meta:
        model = a_cylinder
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

AcylinderFormSet = inlineformset_factory(
    Project, a_cylinder, form=AcylinderForm, extra=1
)

class AdodecahedronForm(forms.ModelForm):

    class Meta:
        model = a_dodecahedron
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

AdodecahedronFormSet = inlineformset_factory(
    Project, a_dodecahedron, form=AdodecahedronForm, extra=1
)

class AsphereForm(forms.ModelForm):

    class Meta:
        model = a_sphere
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

AsphereFormSet = inlineformset_factory(
    Project, a_sphere, form=AsphereForm, extra=1
)

class AicosahedronForm(forms.ModelForm):

    class Meta:
        model = a_icosahedron
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

AicosahedronFormSet = inlineformset_factory(
    Project, a_icosahedron, form=AicosahedronForm, extra=1
)

class AplaneForm(forms.ModelForm):

    class Meta:
        model = a_plane
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

AplaneFormSet = inlineformset_factory(
    Project, a_plane, form=AplaneForm, extra=1
)

class AskyForm(forms.ModelForm):

    class Meta:
        model = a_sky
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

AskyFormSet = inlineformset_factory(
    Project, a_sky, form=AskyForm, extra=1
)
