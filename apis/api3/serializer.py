from rest_framework import serializers

from .models import Company2
class Companysr(serializers.ModelSerializer):
    class Meta:
        model = Company2
        fields = '__all__'