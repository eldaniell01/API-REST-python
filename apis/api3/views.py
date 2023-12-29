from django.shortcuts import render
from rest_framework import viewsets
from .serializer import Companysr
from .models import Company2

# Create your views here.
class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company2.objects.all()
    serializer_class=Companysr