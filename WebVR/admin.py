from django.contrib import admin

from .models import *

admin.site.site_header = "WebVR"

# Register your models here.
class AboxInLine(admin.TabularInline):
    model = a_box
    extra=0

class AcircleInLine(admin.TabularInline):
    model = a_circle
    extra=0

class AconeInLine(admin.TabularInline):
    model = a_cone
    extra=0

class AcylinderInLine(admin.TabularInline):
    model = a_cylinder
    extra=0

class AdodecahedronInLine(admin.TabularInline):
    model = a_dodecahedron
    extra=0


class AsphereInLine(admin.TabularInline):
    model = a_sphere
    extra=0


class AskyInLine(admin.TabularInline):
    model = a_sky
    extra=0



class ProjectAdmin(admin.ModelAdmin):

    list_display=("name", "creator")

    inlines = [
        AboxInLine,
        AcircleInLine,
        AconeInLine,
        AcylinderInLine,
        AdodecahedronInLine,
        AsphereInLine,
        AskyInLine,
    ]

admin.site.register(Project, ProjectAdmin)
