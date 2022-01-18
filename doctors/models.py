from django.db import models
import uuid
from django.db.models.deletion import CASCADE
from users.models import User

# Create your models here.
class Doctor(models.Model):
    title_choices = (
        ('Dr.','Dr.'),
        ('Prof', 'Prof')
    )
    title = models.CharField(max_length=254, choices=title_choices)
    name = models.CharField(max_length=254, null=False, blank=False)
    email = models.EmailField()
    work_number = models.IntegerField(unique=True)
    speciality = models.CharField(max_length=254)


    def __str__(self):
        return str(self.name)

class Appointment(models.Model):
    appointment_no = models.AutoField(primary_key=True)
    appointment_id = models.UUIDField(default=uuid.uuid4, editable=False)
    date_of_appointment = models.DateTimeField(null=True)
    client = models.ForeignKey(User, on_delete=CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=CASCADE)
    comment = models.CharField(max_length=254, null=True, blank=True)
    

    def __str__(self):
        return str(self.appointment_id)