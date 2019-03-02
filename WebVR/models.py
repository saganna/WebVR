from django.db.models import *
from colorful.fields import RGBColorField

# Create your models here.

#Basic Models
class Basic(Model):
    pass

class animation(Basic):#animation class
    
    pass

class position(Basic):#position class
    pos_basic = OneToOneField(Basic, parent_link=True, on_delete=CASCADE)

    pos_x=FloatField(default=0)
    pos_y=FloatField(default=0)
    pos_z=FloatField(default=0)

    def pos(self):
        return "{} {} {}".format(self.pos_x, self.pos_y, self.pos_z)

class rotation(Basic):#rotation class
    rot_basic = OneToOneField(Basic, parent_link=True, on_delete=CASCADE)

    rot_x=FloatField(default=0)
    rot_y=FloatField(default=0)
    rot_z=FloatField(default=0)

    def rot(self):
        return "{} {} {}".format(self.rot_x, self.rot_y, self.rot_z)
    
class scale(Basic):#scale class
    sca_basic = OneToOneField(Basic, parent_link=True, on_delete=CASCADE)

    sca_x=FloatField(default=1)
    sca_y=FloatField(default=1)
    sca_z=FloatField(default=1)

    def sca(self):
        return "{} {} {}".format(self.sca_x, self.sca_y, self.sca_z)
    
class shadow(Basic):#shadow class
    sha_basic = OneToOneField(Basic, parent_link=True, on_delete=CASCADE)

    cast=BooleanField(default=False)
    receive=BooleanField(default=False)

class Basemodel(shadow, rotation, position, scale):
    name = CharField(max_length=50)
    color = RGBColorField(default='#FF0000')
    src = TextField(default="")#change to url
    visible = BooleanField(default=False)

    class Meta:
        abstract=True

#project Model
class Project(Model):
    name = CharField(max_length=200, default="empty")
    changed_date = DateField()
    description = TextField()

    def __str__(self):
        return self.name

#real object Models
class a_box(Basemodel):
    project = ForeignKey(Project, on_delete=CASCADE)

    depth = FloatField(default=1)
    height = FloatField(default=1)
    width = FloatField(default=1)

    def __str__(self):
        return self.name

class a_circle(Basemodel):
    project = ForeignKey(Project, on_delete=CASCADE)

    radius = FloatField(default=1)
    height = FloatField(default=256)
    width = FloatField(default=512)
    theta_length = FloatField(default=360)
    theta_start = FloatField(default=0)

    def __str__(self):
        return self.name

class a_cone(Basemodel):
    project = ForeignKey(Project, on_delete=CASCADE)

    radius_bottom = FloatField(default=1)
    radius_top = FloatField(default=0.8)
    theta_length = FloatField(default=360)
    theta_start = FloatField(default=0)
    width = FloatField(default=512)
    height = FloatField(default=256)

    def __str__(self):
        return self.name

class a_cylinder(Basemodel):
    project = ForeignKey(Project, on_delete=CASCADE)

    radius_bottom = FloatField(default=1)
    radius_top = FloatField(default=0.8)
    theta_length = FloatField(default=360)
    theta_start = FloatField(default=0)
    width = FloatField(default=512)
    height = FloatField(default=256)
    open_ended = BooleanField(default=False)
    
    def __str__(self):
        return self.name

class a_dodecahedron(Basemodel):
    project = ForeignKey(Project, on_delete=CASCADE)

    pass

class a_sphere(Basemodel):
    project = ForeignKey(Project, on_delete=CASCADE)

    height = FloatField(256)
    radius = FloatField(1)
    theta_length = FloatField(default=180)
    theta_start = FloatField(default=0)
    width = FloatField(default=512)
    
    def __str__(self):
        return self.name
