from django.db.models import *
from colorful.fields import RGBColorField
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.

#Basic Models
class Basic(Model):
    pass

class animation(Basic):#animation class

    pass

class position(Basic):#position class
    pos_basic = OneToOneField(Basic, parent_link=True, on_delete=CASCADE)

    pos_x=DecimalField(default=0, max_digits=5, decimal_places=2)
    pos_y=DecimalField(default=0, max_digits=5, decimal_places=2)
    pos_z=DecimalField(default=-4, max_digits=5, decimal_places=2)

    def pos(self):
        return "{} {} {}".format(self.pos_x, self.pos_y, self.pos_z)

class rotation(Basic):#rotation class
    rot_basic = OneToOneField(Basic, parent_link=True, on_delete=CASCADE)

    rot_x=DecimalField(default=0, max_digits=5, decimal_places=2)
    rot_y=DecimalField(default=0, max_digits=5, decimal_places=2)
    rot_z=DecimalField(default=0, max_digits=5, decimal_places=2)

    def rot(self):
        return "{} {} {}".format(self.rot_x, self.rot_y, self.rot_z)

class scale(Basic):#scale class
    sca_basic = OneToOneField(Basic, parent_link=True, on_delete=CASCADE)

    sca_x=DecimalField(default=1, max_digits=5, decimal_places=2)
    sca_y=DecimalField(default=1, max_digits=5, decimal_places=2)
    sca_z=DecimalField(default=1, max_digits=5, decimal_places=2)

    def sca(self):
        return "{} {} {}".format(self.sca_x, self.sca_y, self.sca_z)

class shadow(Basic):#shadow class
    sha_basic = OneToOneField(Basic, parent_link=True, on_delete=CASCADE)

    cast=BooleanField(default=False)
    receive=BooleanField(default=False)

class Basemodel(shadow, rotation, position, scale):
    name = CharField(max_length=50)
    color = RGBColorField(default='#FF0000')
    visible = BooleanField(default=True)

    class Meta:
        abstract=True

class AutoDateTimeField(DateTimeField):
    def pre_save(self, model_instance, add):
        return timezone.now()

#project Model
class UserDATA(Model):
    creator = ForeignKey(User, editable=False, on_delete=CASCADE)
    class meta:
        abstract = True

class Project(UserDATA):
    name = CharField(max_length=200, blank=False)
    description = TextField()
    created_date = DateField(default=timezone.now)
    updated_date = AutoDateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('show project', kwargs={'name' : self.name})

#real object Models
class a_box(Basemodel):
    project = ForeignKey(Project, on_delete=CASCADE)

    depth = DecimalField(default=1, max_digits=5, decimal_places=2)
    height = DecimalField(default=1, max_digits=5, decimal_places=2)
    width = DecimalField(default=1, max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name

class a_circle(Basemodel):
    project = ForeignKey(Project, on_delete=CASCADE)

    radius = DecimalField(default=1, max_digits=5, decimal_places=2)
    height = DecimalField(default=256, max_digits=5, decimal_places=2)
    width = DecimalField(default=512, max_digits=5, decimal_places=2)
    theta_length = DecimalField(default=360, max_digits=5, decimal_places=2)
    theta_start = DecimalField(default=0, max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name

class a_cone(Basemodel):
    project = ForeignKey(Project, on_delete=CASCADE)

    radius_bottom = DecimalField(default=1, max_digits=5, decimal_places=2)
    radius_top = DecimalField(default=0.8, max_digits=5, decimal_places=2)
    theta_length = DecimalField(default=360, max_digits=5, decimal_places=2)
    theta_start = DecimalField(default=0, max_digits=5, decimal_places=2)
    width = DecimalField(default=512, max_digits=5, decimal_places=2)
    height = DecimalField(default=256, max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name

class a_cylinder(Basemodel):
    project = ForeignKey(Project, on_delete=CASCADE)

    radius = DecimalField(default=1, max_digits=5, decimal_places=2)
    theta_length = DecimalField(default=360, max_digits=5, decimal_places=2)
    theta_start = DecimalField(default=0, max_digits=5, decimal_places=2)
    width = DecimalField(default=512, max_digits=5, decimal_places=2)
    height = DecimalField(default=1, max_digits=5, decimal_places=2)
    open_ended = BooleanField(default=False)

    def __str__(self):
        return self.name

class a_dodecahedron(Basemodel):
    project = ForeignKey(Project, on_delete=CASCADE)

    radius = DecimalField(default=1, max_digits=5, decimal_places=2)

    pass

class a_sphere(Basemodel):
    project = ForeignKey(Project, on_delete=CASCADE)

    height = DecimalField(default=256, max_digits=5, decimal_places=2)
    radius = DecimalField(default=1, max_digits=5, decimal_places=2)
    theta_length = DecimalField(default=180, max_digits=5, decimal_places=2)
    theta_start = DecimalField(default=0, max_digits=5, decimal_places=2)
    width = DecimalField(default=512, max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name

class a_icosahedron(Basemodel):
    project = ForeignKey(Project, on_delete=CASCADE)

    height = DecimalField(default=256, max_digits=5, decimal_places=2)
    radius = DecimalField(default=1, max_digits=5, decimal_places=2)
    width = DecimalField(default=512, max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name

class a_plane(Basemodel):
    project = ForeignKey(Project, on_delete=CASCADE)

    height = DecimalField(default=1, max_digits=5, decimal_places=2)
    width = DecimalField(default=1, max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name

class a_sky(Basic):
    sky_basic = OneToOneField(Basic, parent_link=True, on_delete=CASCADE)
    project = ForeignKey(Project, on_delete=CASCADE)

    name = CharField(max_length=50)
    color = RGBColorField(default='#6EBAA7')
    visible = BooleanField(default=True)

    radius = DecimalField(default=5000, max_digits=10, decimal_places=5)
    opacity = DecimalField(default=1, max_digits=5, decimal_places=2)
    theta_start = DecimalField(default=0, max_digits=5, decimal_places=2)
    theta_length = DecimalField(default=180, max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name
