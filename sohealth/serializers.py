from rest_framework import serializers
from .models import Hospitalization


class HospitalizationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Hospitalization
        fields = ('Campos view',
                  'Campos view',
                  'Campos view'
        )
        