from django.urls import path
 
from rest_framework.routers import SimpleRouter
 
from .views import HospitalizationViewSet, HospitalizationAPIView
 
router = SimpleRouter()
router.register('internacao', HospitalizationViewSet)
urlpatterns = [
    path('internacao/', HospitalizationAPIView.as_view(), name='beneficiarios'),
]
