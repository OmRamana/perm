from rest_framework import routers
from health.api import doctorViewSet, clientViewSet, appointmentViewSet


router = routers.DefaultRouter()
router.register('api/doctor',doctorViewSet,'doctors')
router.register('api/client',clientViewSet,'clients')
router.register('api/appointments',clientViewSet,'appointments')

urlpatterns = router.urls