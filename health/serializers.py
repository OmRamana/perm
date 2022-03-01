from rest_framework import serializers
from health.models import doctor, client, appointment

class doctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = doctor
        fields ='__all__'

class clientSerializer(serializers.ModelSerializer):
    class Meta:
        model = client
        fields = '__all__'

class appointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = appointment
        fields = '__all__'