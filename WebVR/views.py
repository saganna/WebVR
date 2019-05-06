from django.shortcuts import render, get_object_or_404
from django.views.generic import *

from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.db import transaction
from .models import *
from .forms import *

# Create your views here.
def Home(request):
    template='WebVR/Home.html'
    content={'projects' : Project}
    return render(request, template, content)

def CreateProject(request):
    template='WebVR/createVR.html'
    if request.method=='POST':
        form = ProjectForm(request.POST, request.FILES)

        if form.is_valid():
            project = form.save()
            project.save()
    else :
        form = ProjectForm()

    print(form)
    return render(request, template, {'form':form,})

class ProjectListView(ListView):
    model = Project
    template_name = 'WebVR/projects.html'
    context_object_name = 'projects'
    ordering = ['-updated_date']
    paginate_by = 2

class UserProjectListView(ListView):
    model = Project
    template_name = 'WebVR/user_projects.html'
    context_object_name = 'projects'
    ordering = ['-updated_date']
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Project.objects.filter(creator=user).order_by('-updated_date')

class ProjectCreateView(LoginRequiredMixin, CreateView):
    model = Project
    template_name='WebVR/createVR.html'
    fields=['name', 'description']

'''
    def get_context_data(self, **kwargs):
        data = super(ProjectCreateView, self).get_context_data(**kwargs)
        if self.request.POST:
            print(AboxFormSet(self.request.POST))
            data['abox'] = AboxFormSet(self.request.POST)
            #data['acircle'] = AcircleFormSet(self.request.POST)
            #data['acone'] = AconeFormSet(self.request.POST)
            #data['acylinder'] = AcylinderFormSet(self.request.POST, instance=self.object)
            #data['adodecahedron'] = AdodecahedronFormSet(self.request.POST)
            #data['asphere'] = AsphereFormSet(self.request.POST)
            #data['aicosahedron'] = AicosahedronFormSet(self.request.POST)
            #data['aplane'] = AplaneFormSet(self.request.POST)
            #data['asky'] = AskyFormSet(self.request.POST)
        else:
            data['abox'] = AboxFormSet()
            #data['acircle'] = AcircleFormSet()
            #data['acone'] = AconeFormSet()
            #data['acylinder'] = AcylinderFormSet()
            #data['adodecahedron'] = AdodecahedronFormSet()
            #data['asphere'] = AsphereFormSet()
            #data['aicosahedron'] = AicosahedronFormSet()
            #data['aplane'] = AplaneFormSet()
            #data['asky'] = AskyFormSet()
        return data

    def form_valid(self, form):
        context = self.get_context_data()

        abox = context['abox']
        #acircle = context['acircle']
        #acone = context['acone']
        #acylinder = context['acylinder']
        #adodecahedron = context['adodecahedron']
        #asphere = context['asphere']
        #aicosahedron = context['aicosahedron']
        #aplane = context['aplane']
        #asky = context['asky']
        with transaction.atomic():
            form.instance.creator = self.request.user
            self.object = form.save()
            if abox.is_valid():# and acircle.is_valid() and acone.is_valid() and acylinder.is_valid() and adodecahedron.is_valid() and asphere.is_valid() and aicosahedron.is_valid() and aplane.is_valid() and asky.is_valid():
                abox.instance = self.object
                #acircle.instance = self.object
                #acircle.save()
                #acone.instance = self.object
                #acone.save()
                #acylinder.instance = self.object
                #acylinder.save()
                #adodecahedron.instance = self.object
                #adodecahedron.save()
                #asphere.instance = self.object
                #asphere.save()
                #aicosahedron.instance = self.object
                #aicosahedron.save()
                #aplane.instance = self.object
                #aplane.save()
                #asky.instance = self.object
                #asky.save()
        return super(ProjectCreateView, self).form_valid(form)
'''
class ProjectUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Project
    template_name='WebVR/updateVR.html'
    fields=['name', 'description']

    def get_context_data(self, **kwargs):
        data = super(ProjectUpdateView, self).get_context_data(**kwargs)
        if self.request.POST:
            data['abox'] = AboxFormSet(self.request.POST, instance=self.object)
            data['acircle'] = AcircleFormSet(self.request.POST, instance=self.object)
            data['acone'] = AconeFormSet(self.request.POST, instance=self.object)
            data['acylinder'] = AcylinderFormSet(self.request.POST, instance=self.object)
            data['adodecahedron'] = AdodecahedronFormSet(self.request.POST, instance=self.object)
            data['asphere'] = AsphereFormSet(self.request.POST, instance=self.object)
            data['aicosahedron'] = AicosahedronFormSet(self.request.POST, instance=self.object)
            data['aplane'] = AplaneFormSet(self.request.POST, instance=self.object)
            data['asky'] = AskyFormSet(self.request.POST, instance=self.object)
        else:
            data['abox'] = AboxFormSet(instance=self.object)
            data['acircle'] = AcircleFormSet(instance=self.object)
            data['acone'] = AconeFormSet(instance=self.object)
            data['acylinder'] = AcylinderFormSet(instance=self.object)
            data['adodecahedron'] = AdodecahedronFormSet(instance=self.object)
            data['asphere'] = AsphereFormSet(instance=self.object)
            data['aicosahedron'] = AicosahedronFormSet(instance=self.object)
            data['aplane'] = AplaneFormSet(instance=self.object)
            data['asky'] = AskyFormSet(instance=self.object)
        return data

    def form_valid(self, form):
        context = self.get_context_data()

        abox = context['abox']
        acircle = context['acircle']
        acone = context['acone']
        acylinder = context['acylinder']
        adodecahedron = context['adodecahedron']
        asphere = context['asphere']
        aicosahedron = context['aicosahedron']
        aplane = context['aplane']
        asky = context['asky']
        with transaction.atomic():
            form.instance.creator = self.request.user
            self.object = form.save()
            if abox.is_valid() and acircle.is_valid() and acone.is_valid() and acylinder.is_valid() and adodecahedron.is_valid() and asphere.is_valid() and aicosahedron.is_valid() and aplane.is_valid() and asky.is_valid():

                abox.instance = self.object
                abox.save()
                acircle.instance = self.object
                acircle.save()
                acone.instance = self.object
                acone.save()
                acylinder.instance = self.object
                acylinder.save()
                adodecahedron.instance = self.object
                adodecahedron.save()
                asphere.instance = self.object
                asphere.save()
                aicosahedron.instance = self.object
                aicosahedron.save()
                aplane.instance = self.object
                aplane.save()
                asky.instance = self.object
                asky.save()
        return super(ProjectUpdateView, self).form_valid(form)

    def test_func(self):
        project = self.get_object()
        if self.request.user == project.creator:
            return True
        return False

class ProjectDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Project
    success_url = 'WebVR/projects/'

    def test_func(self):
        project = self.get_object()
        if self.request.user == project.creator:
            return True
        return False

def showproject_view(request, pk):
    obj = Project.objects.get(id=pk)
    context={}

    #adding abox
    abox=[]
    for i in range(obj.a_box_set.count()):
        temp={}
        t=obj.a_box_set.all()[i]
        temp['name']=t.name
        temp['color']=t.color
        temp['visible']=t.visible
        #temp['position']=t.position
        #temp['rotation']=t.rotation
        #temp['scale']=t.scale
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
        #temp['position']=t.position
        #temp['rotation']=t.rotation
        temp['radius']=t.radius
        #temp['scale']=t.scale
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
        #temp['position']=t.position
        #temp['rotation']=t.rotation
        #temp['scale']=t.scale
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
        #temp['position']=t.position
        #temp['rotation']=t.rotation
        #temp['scale']=t.scale
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
        #temp['position']=t.position
        #temp['rotation']=t.rotation
        #temp['scale']=t.scale
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
        #temp['position']=t.position
        #temp['rotation']=t.rotation
        #temp['scale']=t.scale
        temp['height']=t.height
        temp['width']=t.width
        temp['theta_length']=t.theta_length
        temp['theta_start']=t.theta_start
        temp['radius']=t.radius
        temp['shadow']="cast : {} receive : {}".format(t.cast, t.receive)
        asphere.append(temp)
    context['a_sphere']=asphere

    #adding aicosahedron
    aicosahedron=[]
    for i in range(obj.a_icosahedron_set.count()):
        temp={}
        t=obj.a_icosahedron_set.all()[i]
        temp['name']=t.name
        temp['color']=t.color
        temp['visible']=t.visible
        #temp['position']=t.position
        #temp['rotation']=t.rotation
        #temp['scale']=t.scale
        temp['height']=t.height
        temp['width']=t.width
        temp['radius']=t.radius
        temp['shadow']="cast : {} receive : {}".format(t.cast, t.receive)
        aicosahedron.append(temp)
    context['a_icosahedron']=aicosahedron

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

    #adding aplane
    aplane=[]
    for i in range(obj.a_plane_set.count()):
        temp={}
        t=obj.a_plane_set.all()[i]
        temp['name']=t.name
        temp['color']=t.color
        temp['visible']=t.visible
        temp['height']=t.height
        temp['width']=t.width
        aplane.append(temp)
    context['a_plane']=aplane

    return render(request, "WebVR/showproject.html", context)
