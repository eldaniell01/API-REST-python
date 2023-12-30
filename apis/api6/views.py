from django.shortcuts import render

from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import viewsets
from .serializer import Tasksr
from .models import Task

# Create your views here.

@extend_schema_view(
    list= extend_schema(description='obtiene una lista de tareas'),
    retrieve=extend_schema(description='obtiene una tarea'),
    create=extend_schema(description='crea una tarea'),
    update=extend_schema(description='actualizar tarea'),
    destroy=extend_schema(description='eliminar tarea'),
)
class TaskViewSet(viewsets.ModelViewSet):
    serializer_class=Tasksr
    queryset = Task.objects.all()