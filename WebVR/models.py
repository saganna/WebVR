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


class rotation(Basic):#rotation class
    rot_basic = OneToOneField(Basic, parent_link=True, on_delete=CASCADE)

    rot_x=FloatField(default=0)
    rot_y=FloatField(default=0)
    rot_z=FloatField(default=0)

    
class scale(Basic):#scale class
    sca_basic = OneToOneField(Basic, parent_link=True, on_delete=CASCADE)

    sca_x=FloatField(default=1)
    sca_y=FloatField(default=1)
    sca_z=FloatField(default=1)

    
class shadow(Basic):#shadow class
    sha_basic = OneToOneField(Basic, parent_link=True, on_delete=CASCADE)

    cast=BooleanField(default=False)
    receive=BooleanField(default=False)



class Basemodel(shadow, rotation, position, scale):
    name = CharField(max_length=50)
    color = RGBColorField(default=['#FF0000', '#00FF00', '#0000FF'])
    src = TextField(default="")#change to url
    visible = BooleanField(default=False)

    #ani = ForeignKey(animation, on_delete=CASCADE)
    #pos = ForeignKey(position, on_delete=CASCADE)
    #rot = ForeignKey(rotation, on_delete=CASCADE)
    #sca = ForeignKey(scale, on_delete=CASCADE)
    #sha = ForeignKey(shadow, on_delete=CASCADE)

    class Meta:
        abstract=True


#real object Models
class abox(Basemodel):
    depth = FloatField(default=1)
    height = FloatField(default=1)
    width = FloatField(default=1)

    def __str__(self):
        return self.name

class acircle(Basemodel):
    radius = FloatField(default=1)
    height = FloatField(default=256)
    width = FloatField(default=512)
    theta_length = FloatField(default=360)
    theta_start = FloatField(default=0)

    def __str__(self):
        return self.name
