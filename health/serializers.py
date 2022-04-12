from rest_framework import serializers
from health.models import doctor, client, appointment
from django.contrib.auth.models import User

class appointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = appointment
        fields = '__all__'    


    
    
        

