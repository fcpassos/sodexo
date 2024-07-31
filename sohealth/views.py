from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend, DateTimeFilter, DateFilter, DateFromToRangeFilter
from django_filters.rest_framework import NumberFilter, FilterSet, AllValuesFilter
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework import generics
from rest_framework.generics import get_object_or_404
from datetime import timedelta

 
from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import mixins


from .models import Hospitalization
from .serializers import HospitalizationSerializer


class HospitalizationAPIView(generics.ListCreateAPIView):
    queryset = Hospitalization.objects.all()
    serializer_class = HospitalizationSerializer
 
    def get_queryset(self):
        if self.kwargs.get('IdLeito'):
            return self.queryset.filter(locator=self.kwargs.get('IdLeito'))
        return self.queryset.all()
    
    
class HospitalizationViewSet(
#    mixins.ListModelMixin,
#    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
#    mixins.UpdateModelMixin,
#    mixins.DestroyModelMixin,
    viewsets.GenericViewSet
    ):
    queryset = Hospitalization.objects.all()
    serializer_class = HospitalizationSerializer
