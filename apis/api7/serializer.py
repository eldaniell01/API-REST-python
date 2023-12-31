from rest_framework import serializers
from .models import Category, Product

class Productsr(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        
class Categorysr(serializers.ModelSerializer):
    productR = Productsr(many=True, read_only=True)
    class Meta:
        model = Category
        fields = '__all__'