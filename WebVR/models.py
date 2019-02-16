from django.db import models
from colorful.fields import RGBColorField

# Create your models here.
class a_box(models.Model):
    name = models.CharField(max_length=50)
    color = RGBColorField(colors=['#FF0000', '#00FF00', '#0000FF'])
    depth = models.FloatField()
    height = models.FloatField()
    width = models.FloatField()
    src = models.CharField(max_length=100)