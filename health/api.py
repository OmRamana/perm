from health.models import doctor,client,appointment
from rest_framework import viewsets
from health.serializers import doctorSerializer,clientSerializer,appointmentSerializer
from rest_framework.permissions import IsAuthenticated 



class doctorViewSet(viewsets.ModelViewSet):
    queryset = doctor.objects.all()
    serializer_class = doctorSerializer
    permission_classes = (IsAuthenticated,) 

class clientViewSet(viewsets.ModelViewSet):
    queryset = client.objects.all()
    serializer_class = clientSerializer
    permission_classes = (IsAuthenticated,) 

class appointmentViewSet(viewsets.ModelViewSet):
    queryset = client.objects.all()
    serializer_class = appointmentSerializer
    permission_classes = (IsAuthenticated,) 

   


