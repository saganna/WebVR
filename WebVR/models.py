from django.db.models import *
from colorful.fields import RGBColorField

# Create your models here.

#Basic Models
class Basemodel(Model, animation_class, position_class, rotation_class, scale_class, shadow_class):
    name = CharField(max_length=50)
    color = RGBColorField(colors=['#FF0000', '#00FF00', '#0000FF'])
    src = TextField()
    visible = BooleanField()

class animation_class(Model):
    pass

class position_class(Model):
    x=FloatField()
    y=FloatField()
    z=FloatField()
    
class rotation_class(Model):
    x=FloatField()
    y=FloatField()
    z=FloatField()
    
class scale_class(Model):
    x=FloatField()
    y=FloatField()
    z=FloatField()

class shadow_class(Model):
    cast=BooleanField()
    receive=BooleanField()


#real object Models
class a_box(Model, Basemodel):
    depth = FloatField()
    height = FloatField()
    width = FloatField()

class a_circle(Model, Basemodel):
    radius=FloatField()
    theta_length=FloatField()
    theta_start=FloatField()