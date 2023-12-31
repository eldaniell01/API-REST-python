from django.shortcuts import render
from rest_framework import viewsets
from .serializer import Categorysr, Productsr
from .models import Category, Product
# Create your views here.

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = Categorysr
    
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = Productsr
