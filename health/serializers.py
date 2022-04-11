from rest_framework import serializers
from health.models import doctor, client, appointment
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']

class appointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = appointment
        fields = '__all__'    

class doctorSerializer(serializers.ModelSerializer):
    my_appointments = appointmentSerializer(many = True, source = 'doc')
    class Meta:
        model = doctor
        fields ='__all__'

class clientSerializer(serializers.ModelSerializer):
    my_appointments = appointmentSerializer(many = True, source = 'client')
    class Meta:
        model = client
        fields = '__all__'
    
    
        

