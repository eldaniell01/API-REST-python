from django.shortcuts import render
from rest_framework import viewsets
from .serializer import Programmersr
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import authentication_classes
from rest_framework.authentication import TokenAuthentication
from .models import Programmer
# Create your views here.


class ProgramerViewSet(viewsets.ModelViewSet):
    queryset = Programmer.objects.all()
    serializer_class=Programmersr
    permission_classes=[IsAuthenticated]
   
