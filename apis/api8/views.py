from django.shortcuts import render
from rest_framework import viewsets, permissions
from .serializer import Motosr, Proveedorsr, Repuestosr
from .models import Moto, Proveedor, Repuesto
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
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
    """@action(detail=False, methods=['POST'])
    def create_prodcut(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)"""
    
