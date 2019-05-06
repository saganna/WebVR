from django import forms
from django.forms.models import inlineformset_factory

from .models import *

class ProjectForm(forms.ModelForm):
    class Meta :
        model = Project
        exclude=[]

    def as_django_admin(self):
        from formadmin.forms import as_django_admin
        return as_django_admin(self)


class AboxForm(forms.ModelForm):

    class Meta:
        model = a_box
        exclude=[]

AboxFormSet = inlineformset_factory(
    Project, a_box, form=AboxForm, extra=2
)

class AcircleForm(forms.ModelForm):

    class Meta:
        model = a_circle
        exclude=[]

AcircleFormSet = inlineformset_factory(
    Project, a_circle, form=AcircleForm, extra=1
)

class AconeForm(forms.ModelForm):

    class Meta:
        model = a_cone
        exclude=[]

AconeFormSet = inlineformset_factory(
    Project, a_cone, form=AconeForm, extra=1
)

class AcylinderForm(forms.ModelForm):

    class Meta:
        model = a_cylinder
        exclude=[]

AcylinderFormSet = inlineformset_factory(
    Project, a_cylinder, form=AcylinderForm, extra=1
)

class AdodecahedronForm(forms.ModelForm):

    class Meta:
        model = a_dodecahedron
        exclude=[]

AdodecahedronFormSet = inlineformset_factory(
    Project, a_dodecahedron, form=AdodecahedronForm, extra=1
)

class AsphereForm(forms.ModelForm):

    class Meta:
        model = a_sphere
        exclude=[]

AsphereFormSet = inlineformset_factory(
    Project, a_sphere, form=AsphereForm, extra=1
)

class AicosahedronForm(forms.ModelForm):

    class Meta:
        model = a_icosahedron
        exclude=[]

AicosahedronFormSet = inlineformset_factory(
    Project, a_icosahedron, form=AicosahedronForm, extra=1
)

class AplaneForm(forms.ModelForm):

    class Meta:
        model = a_plane
        exclude=[]

AplaneFormSet = inlineformset_factory(
    Project, a_plane, form=AplaneForm, extra=1
)

class AskyForm(forms.ModelForm):

    class Meta:
        model = a_sky
        exclude=[]

AskyFormSet = inlineformset_factory(
    Project, a_sky, form=AskyForm, extra=1
)
