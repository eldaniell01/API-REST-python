from django.shortcuts import render
from rest_framework import viewsets
from .serializer import Programmersr
from .models import Programmer
# Create your views here.

class ProgramerViewSet(viewsets.ModelViewSet):
    queryset = Programmer.objects.all()
    serializer_class=Programmersr
