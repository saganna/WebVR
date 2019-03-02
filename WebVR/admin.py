from django.contrib import admin

from .models import *

# Register your models here.
class AboxInLine(admin.TabularInline):
    model = a_box

class ProjectAdmin(admin.ModelAdmin):
    inlines = [
        AboxInLine,
    ]

admin.site.register(Project, ProjectAdmin)