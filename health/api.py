from health.models import doctor,client,appointment
from rest_framework import viewsets
from health.serializers import doctorSerializer,clientSerializer,appointmentSerializer
from rest_framework.permissions import IsAuthenticated 



class doctorViewSet(viewsets.ModelViewSet):
    queryset = doctor.objects.all()
    serializer_class = doctorSerializer
    

class clientViewSet(viewsets.ModelViewSet):
    queryset = client.objects.all()
    serializer_class = clientSerializer
    

class appointmentViewSet(viewsets.ModelViewSet):
    queryset = appointment.objects.all()
    serializer_class = appointmentSerializer
   

   


