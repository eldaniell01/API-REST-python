from django.shortcuts import render
from rest_framework import viewsets
from .serializer import Motosr, Proveedorsr, Repuestosr
from .models import Moto, Proveedor, Repuesto
# Create your views here.

class MotoViewSet(viewsets.ModelViewSet):
    queryset = Moto.objects.all()
    serializer_class = Motosr

class ProveedorViewSet(viewsets.ModelViewSet):
    queryset = Proveedor.objects.all()
    serializer_class = Proveedorsr
    
class RepuestoViewSet(viewsets.ModelViewSet):
    queryset = Repuesto.objects.all()
    serializer_class = Repuestosr