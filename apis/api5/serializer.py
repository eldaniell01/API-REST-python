from rest_framework import serializers
from .models import Book

class Booksr(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField()
    number_of_pages = serializers.IntegerField()
    quantity = serializers.IntegerField()
    publish_date = serializers.DateField()
    
    def create(self, data):
        return Book.objects.create(**data)