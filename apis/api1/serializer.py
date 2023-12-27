from rest_framework import serializers

from .models import Programmer
class Programmersr(serializers.ModelSerializer):
    class Meta:
        model = Programmer
        fields = '__all__'