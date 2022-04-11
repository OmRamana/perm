from django.db import models
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.dispatch import receiver
from django.db.models.signals import post_save


class doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)             


class client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)    
    

class appointment(models.Model):
    date = models.DateTimeField()
    doctor = models.ForeignKey(doctor,on_delete=models.CASCADE, related_name='doc')
    client = models.ForeignKey(client,on_delete=models.CASCADE, related_name='client')

"""     @receiver(post_save)
    def send_mail_on_create(sender, instance=None, created=False, **kwargs):
        if created:
            send_mail('Rest Email','html content','ramanacomfy@gmail.com',["omramana20@gmail.com"],fail_silently=False,) """

