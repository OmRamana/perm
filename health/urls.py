from rest_framework import routers
from health.api import doctorViewSet, clientViewSet, appointmentViewSet, UserViewSet
from django.urls import path,include


router = routers.DefaultRouter()
router.register(r'doctor',doctorViewSet,'doctors')
router.register(r'client',clientViewSet,'clients')
router.register(r'appointments',appointmentViewSet,'appointments')
router.register(r'users', UserViewSet)


urlpatterns = [
    path('', include(router.urls)),
]

