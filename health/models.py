from django.db import models
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.dispatch import receiver
from django.db.models.signals import post_save
  
class appointment(models.Model):
    date = models.DateTimeField()
    doctor = models.ForeignKey(User,on_delete=models.CASCADE, related_name='doctor_user')
    client = models.ForeignKey(User,on_delete=models.CASCADE, related_name='client_user')

"""     @receiver(post_save)
    def send_mail_on_create(sender, instance=None, created=False, **kwargs):
        if created:
            send_mail('Rest Email','html content','ramanacomfy@gmail.com',["omramana20@gmail.com"],fail_silently=False,) """

