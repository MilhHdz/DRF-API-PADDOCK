from rest_framework import serializers
from .models import Sucursal, Domain


class SucursalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sucursal
        exclude = ['schema_name']


class DomainSerializer(serializers.ModelSerializer):
    class Meta:
        model = Domain
        fields = '__all__'
    
    tenant = SucursalSerializer()