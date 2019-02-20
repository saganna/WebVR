from django.db.models import *
from colorful.fields import RGBColorField

# Create your models here.

#Basic Models
class Basemodel(Model):
    name = CharField(max_length=50)
    color = RGBColorField(colors=['#FF0000', '#00FF00', '#0000FF'])
    src = TextField()
    visible = BooleanField()

    class ani():#animation class
    
        pass

    class pos():#position class
        x=FloatField()
        y=FloatField()
        z=FloatField()

    class rot():#rotation class
        x=FloatField()
        y=FloatField()
        z=FloatField()
    
    class sca():#scale class
        x=FloatField()
        y=FloatField()
        z=FloatField()
    
    class shadow():#shadow class
        cast=BooleanField()
        receive=BooleanField()



#real object Models
class a_box(Basemodel):
    depth = FloatField()
    height = FloatField()
    width = FloatField()

class a_circle(Basemodel):
    radius = FloatField()
    theta_length = FloatField()
    theta_start = FloatField()