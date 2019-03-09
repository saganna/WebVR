from django.shortcuts import render
from django.views.generic import *

from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from django.db import transaction
from .models import *
from .forms import *

# Create your views here.
def Home(request):
    template='WebVR/Home.html'
    content={'projects' : Project}
    return render(request, template, content)

class ProjectListView(ListView):
    model = Project
    template_name = 'WebVR/projects.html'
    context_object_name = 'projects'
    ordering = ['-updated_date']

class ProjectCreateView(CreateView):
    model = Project
    template_name='WebVR/createVR.html'
    success_url = reverse_lazy('project-home')
    fields=['name', 'description']

    def get_context_data(self, **kwargs):
        data = super(ProjectCreateView, self).get_context_data(**kwargs)
        if self.request.POST:
            data['abox'] = AboxFormSet(self.request.POST, instance=self.object)
            data['acircle'] = AcircleFormSet(self.request.POST, instance=self.object)
            data['acone'] = AconeFormSet(self.request.POST, instance=self.object)
        else:
            data['abox'] = AboxFormSet(instance=self.object)
            data['acircle'] = AcircleFormSet(instance=self.object)
            data['acone'] = AconeFormSet(instance=self.object)
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        print(context)
        name = context['abox']
        with transaction.atomic():
            form.instance.creator = self.request.user
            self.object = form.save()
            if name.is_valid():
                name.instance = self.object
                name.save()
        return super(ProjectCreateView, self).form_invalid(form)


def CreateVR_view(request):
    form = ProjectCreateForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProjectCreateForm()

    context = {
        'form' : form
    }
    template='WebVR/createVR.html'
    return render(request, template, context)

def showProject_view(request, id):
    obj = Project.objects.get(id=id)

    context={
        'name' : obj.name,
        'description' : obj.description,
        'created-date' : obj.created_date,
        'updated-date' : obj.updated_date,
    }

    #adding abox
    abox=[]
    for i in range(obj.a_box_set.count()):
        temp={}
        t=obj.a_box_set.all()[i]
        temp['name']=t.name
        temp['color']=t.color
        temp['visible']=t.visible
        temp['position']=t.pos()
        temp['rotation']=t.rot()
        temp['scale']=t.sca()
        temp['depth']=t.depth
        temp['height']=t.height
        temp['width']=t.width
        temp['shadow']="cast : {} receive : {}".format(t.cast, t.receive)
        abox.append(temp)
    context['a_box']=abox


    #adding acircle
    acircle=[]
    for i in range(obj.a_circle_set.count()):
        temp={}
        t=obj.a_circle_set.all()[i]
        temp['name']=t.name
        temp['color']=t.color
        temp['visible']=t.visible
        temp['position']=t.pos()
        temp['rotation']=t.rot()
        temp['scale']=t.sca()
        temp['height']=t.height
        temp['width']=t.width
        temp['theta_length']=t.theta_length
        temp['theta_start']=t.theta_start
        temp['shadow']="cast : {} receive : {}".format(t.cast, t.receive)
        acircle.append(temp)
    context['a_circle']=acircle

    #adding acone
    acone=[]
    for i in range(obj.a_cone_set.count()):
        temp={}
        t=obj.a_cone_set.all()[i]
        temp['name']=t.name
        temp['color']=t.color
        temp['visible']=t.visible
        temp['position']=t.pos()
        temp['rotation']=t.rot()
        temp['scale']=t.sca()
        temp['height']=t.height
        temp['width']=t.width
        temp['theta_length']=t.theta_length
        temp['theta_start']=t.theta_start
        temp['radius_bottom']=t.radius_bottom
        temp['radius_top']=t.radius_top
        temp['shadow']="cast : {} receive : {}".format(t.cast, t.receive)
        acone.append(temp)
    context['a_cone']=acone

    #adding acylinder
    acylinder=[]
    for i in range(obj.a_cylinder_set.count()):
        temp={}
        t=obj.a_cylinder_set.all()[i]
        temp['name']=t.name
        temp['color']=t.color
        temp['visible']=t.visible
        temp['position']=t.pos()
        temp['rotation']=t.rot()
        temp['scale']=t.sca()
        temp['height']=t.height
        temp['width']=t.width
        temp['theta_length']=t.theta_length
        temp['theta_start']=t.theta_start
        temp['radius']=t.radius
        temp['open_ended']=t.open_ended
        temp['shadow']="cast : {} receive : {}".format(t.cast, t.receive)
        acylinder.append(temp)
    context['a_cylinder']=acylinder

    #adding adodecahedron
    adodecahedron=[]
    for i in range(obj.a_dodecahedron_set.count()):
        temp={}
        t=obj.a_dodecahedron_set.all()[i]
        temp['name']=t.name
        temp['color']=t.color
        temp['visible']=t.visible
        temp['position']=t.pos()
        temp['rotation']=t.rot()
        temp['scale']=t.sca()
        temp['radius']=t.radius
        temp['shadow']="cast : {} receive : {}".format(t.cast, t.receive)
        adodecahedron.append(temp)
    context['a_dodecahedron']=adodecahedron

    #adding asphere
    asphere=[]
    for i in range(obj.a_sphere_set.count()):
        temp={}
        t=obj.a_sphere_set.all()[i]
        temp['name']=t.name
        temp['color']=t.color
        temp['visible']=t.visible
        temp['position']=t.pos()
        temp['rotation']=t.rot()
        temp['scale']=t.sca()
        temp['height']=t.height
        temp['width']=t.width
        temp['theta_length']=t.theta_length
        temp['theta_start']=t.theta_start
        temp['radius']=t.radius
        temp['shadow']="cast : {} receive : {}".format(t.cast, t.receive)
        asphere.append(temp)
    context['a_sphere']=asphere

    #adding asky
    asky=[]
    for i in range(obj.a_sky_set.count()):
        temp={}
        t=obj.a_sky_set.all()[i]
        temp['name']=t.name
        temp['color']=t.color
        temp['visible']=t.visible
        temp['theta_length']=t.theta_length
        temp['theta_start']=t.theta_start
        temp['radius']=t.radius
        temp['opacity']=t.opacity
        asky.append(temp)
    context['a_sky']=asky

    print(context)
    return render(request, "WebVR/showproject.html", context)

def showproject_view(request, name):
    obj = Project.objects.get(name=name)
    context={}

    #adding abox
    abox=[]
    for i in range(obj.a_box_set.count()):
        temp={}
        t=obj.a_box_set.all()[i]
        temp['name']=t.name
        temp['color']=t.color
        temp['visible']=t.visible
        temp['position']=t.pos()
        temp['rotation']=t.rot()
        temp['scale']=t.sca()
        temp['depth']=t.depth
        temp['height']=t.height
        temp['width']=t.width
        temp['shadow']="cast : {} receive : {}".format(t.cast, t.receive)
        abox.append(temp)
    context['a_box']=abox


    #adding acircle
    acircle=[]
    for i in range(obj.a_circle_set.count()):
        temp={}
        t=obj.a_circle_set.all()[i]
        temp['name']=t.name
        temp['color']=t.color
        temp['visible']=t.visible
        temp['position']=t.pos()
        temp['rotation']=t.rot()
        temp['radius']=t.radius
        temp['scale']=t.sca()
        temp['height']=t.height
        temp['width']=t.width
        temp['theta_length']=t.theta_length
        temp['theta_start']=t.theta_start
        temp['shadow']="cast : {} receive : {}".format(t.cast, t.receive)
        acircle.append(temp)
    context['a_circle']=acircle

    #adding acone
    acone=[]
    for i in range(obj.a_cone_set.count()):
        temp={}
        t=obj.a_cone_set.all()[i]
        temp['name']=t.name
        temp['color']=t.color
        temp['visible']=t.visible
        temp['position']=t.pos()
        temp['rotation']=t.rot()
        temp['scale']=t.sca()
        temp['height']=t.height
        temp['width']=t.width
        temp['theta_length']=t.theta_length
        temp['theta_start']=t.theta_start
        temp['radius_bottom']=t.radius_bottom
        temp['radius_top']=t.radius_top
        temp['shadow']="cast : {} receive : {}".format(t.cast, t.receive)
        acone.append(temp)
    context['a_cone']=acone

    #adding acylinder
    acylinder=[]
    for i in range(obj.a_cylinder_set.count()):
        temp={}
        t=obj.a_cylinder_set.all()[i]
        temp['name']=t.name
        temp['color']=t.color
        temp['visible']=t.visible
        temp['position']=t.pos()
        temp['rotation']=t.rot()
        temp['scale']=t.sca()
        temp['height']=t.height
        temp['width']=t.width
        temp['theta_length']=t.theta_length
        temp['theta_start']=t.theta_start
        temp['radius']=t.radius
        temp['open_ended']=t.open_ended
        temp['shadow']="cast : {} receive : {}".format(t.cast, t.receive)
        acylinder.append(temp)
    context['a_cylinder']=acylinder

    #adding adodecahedron
    adodecahedron=[]
    for i in range(obj.a_dodecahedron_set.count()):
        temp={}
        t=obj.a_dodecahedron_set.all()[i]
        temp['name']=t.name
        temp['color']=t.color
        temp['visible']=t.visible
        temp['position']=t.pos()
        temp['rotation']=t.rot()
        temp['scale']=t.sca()
        temp['radius']=t.radius
        temp['shadow']="cast : {} receive : {}".format(t.cast, t.receive)
        adodecahedron.append(temp)
    context['a_dodecahedron']=adodecahedron

    #adding asphere
    asphere=[]
    for i in range(obj.a_sphere_set.count()):
        temp={}
        t=obj.a_sphere_set.all()[i]
        temp['name']=t.name
        temp['color']=t.color
        temp['visible']=t.visible
        temp['position']=t.pos()
        temp['rotation']=t.rot()
        temp['scale']=t.sca()
        temp['height']=t.height
        temp['width']=t.width
        temp['theta_length']=t.theta_length
        temp['theta_start']=t.theta_start
        temp['radius']=t.radius
        temp['shadow']="cast : {} receive : {}".format(t.cast, t.receive)
        asphere.append(temp)
    context['a_sphere']=asphere

    #adding asky
    asky=[]
    for i in range(obj.a_sky_set.count()):
        temp={}
        t=obj.a_sky_set.all()[i]
        temp['name']=t.name
        temp['color']=t.color
        temp['visible']=t.visible
        temp['theta_length']=t.theta_length
        temp['theta_start']=t.theta_start
        temp['radius']=t.radius
        temp['opacity']=t.opacity
        asky.append(temp)
    context['a_sky']=asky

    return render(request, "WebVR/showproject.html", context)
