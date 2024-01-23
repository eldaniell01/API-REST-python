from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny
from django.contrib.auth import authenticate, login
from .serializer import Loginsr
# Create your views here.


class LoginView(APIView):
    permission_classes = [AllowAny]
    
    def post (self, request, *args, **kwargs):
        serializer = Loginsr(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            login(request, user)
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.erros, status=status.HTTP_400_BAD_REQUEST)