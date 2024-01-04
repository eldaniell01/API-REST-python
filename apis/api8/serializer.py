from rest_framework import serializers
from .models import Proveedor, Repuesto, Moto

class Proveedorsr(serializers.ModelSerializer):
    class Meta: 
        model = Proveedor
        fields= '__all__'

class Motosr(serializers.ModelSerializer):
    class Meta: 
        model = Moto
        fields= '__all__'

class Repuestosr(serializers.ModelSerializer):
    class Meta: 
        model = Repuesto
        fields= '__all__'