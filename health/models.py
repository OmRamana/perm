from django.db import models

class doctor(models.Model):
    name = models.CharField(max_length=100, blank=True)
    docstatus = models.BooleanField(default=True)

class client(models.Model):
    name = models.CharField(max_length=100, blank=True)
    docstatus = models.BooleanField(default=False)
    doctor = models.ForeignKey(doctor,on_delete=models.CASCADE,blank=True, null=True,related_name='doctor')

class appointment(models.Model):
    date = models.DateTimeField()
    doctor = models.ForeignKey(doctor,on_delete=models.CASCADE, related_name='doc')
    client = models.ForeignKey(client,on_delete=models.CASCADE, related_name='client')

