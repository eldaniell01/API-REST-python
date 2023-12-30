from rest_framework import serializers
from .models import Book
from django.forms import ValidationError

""" class Booksr(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField()
    number_of_pages = serializers.IntegerField()
    quantity = serializers.IntegerField()
    publish_date = serializers.DateField()
    
    def create(self, data):
        return Book.objects.create(**data)
    
    def update(self, instance, data):
        instance.title = data.get('title', instance.title)
        instance.number_of_pages = data.get('number_of_pages', instance.number_of_pages)
        instance.quantity = data.get('quantity', instance.quantity)
        instance.publish_date = data.get('publish_date', instance.publish_date)
        instance.save()
        return instance
         """
class Booksr(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
    
    
