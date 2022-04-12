from health.models import doctor,client,appointment
from rest_framework import viewsets
from health.serializers import doctorSerializer,clientSerializer,appointmentSerializer
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from health.serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated
    

class appointmentViewSet(viewsets.ModelViewSet):       
    serializer_class = appointmentSerializer
    
    def get_queryset(self):
        return  appointment.objects.filter(user_id = self.request.user.id) #filter(doctor = self.request.user.id)
 
    
    

   


