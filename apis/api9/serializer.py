from rest_framework import serializers
from django.contrib.auth import authenticate, login


class Loginsr(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
    
    def validate(self, data):
        username = data.get('username')
        password = data.get('password')
        
        user = authenticate(username=username, password=password)
        if user:
        
            data['user']=user
        else:
            raise serializers.ValidationError('credenciales incorrectas')
        
        return data 