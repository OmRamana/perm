from health.models import doctor,client,appointment
from rest_framework import viewsets
from health.serializers import doctorSerializer,clientSerializer,appointmentSerializer
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from health.serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserSerializer


class doctorViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = doctor.objects.all()
    serializer_class = doctorSerializer
    

class clientViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = client.objects.all()
    serializer_class = clientSerializer
    

class appointmentViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = appointment.objects.all()
    serializer_class = appointmentSerializer
    
    
    

   


