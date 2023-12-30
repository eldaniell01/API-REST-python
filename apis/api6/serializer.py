from .models import Task
from rest_framework import serializers

class Tasksr(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'