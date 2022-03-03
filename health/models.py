from django.db import models
from django.contrib.auth.models import User


class doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    docstatus = models.BooleanField(default=True)           


class client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    docstatus = models.BooleanField(default=False)
    doctor = models.ForeignKey(doctor,on_delete=models.CASCADE,blank=True, null=True,related_name='doctor')

class appointment(models.Model):
    date = models.DateTimeField()
    doctor = models.ForeignKey(doctor,on_delete=models.CASCADE, related_name='doc')
    client = models.ForeignKey(client,on_delete=models.CASCADE, related_name='client')

