from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Book
from .serializer import Booksr

# Create your views here.
@api_view(['GET'])
def book_list(request):
    books = Book.objects.all()
    serializer=Booksr(books, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def book_create(request):
    serializer = Booksr(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors)
    
@api_view(['GET', 'PUT', 'DELETE'])   
def book(request, pk):
    if request.method == 'GET':
        book = Book.objects.get(pk=pk)
        serializer = Booksr(book)
        return Response(serializer.data)