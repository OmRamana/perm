from django.db import models

class doctor(models.Model):
    name = models.CharField(max_length=100, blank=True)

class client(models.Model):
    name = models.CharField(max_length=100, blank=True)
    doctor = models.ForeignKey(doctor,on_delete=models.CASCADE,related_name='doctor')

class appointment(models.Model):
    date = models.DateTimeField()
    doctor = models.ForeignKey(doctor,on_delete=models.CASCADE, related_name='doc')
    client = models.ForeignKey(client,on_delete=models.CASCADE, related_name='client')
