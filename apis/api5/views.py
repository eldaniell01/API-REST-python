from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView
from .models import Book
from .serializer import Booksr

# Create your views here.
""" @api_view(['GET'])
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
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET', 'PUT', 'DELETE'])   
def book(request, pk):
    try: 
        book = Book.objects.get(pk=pk)
    except:
        return Response({
            'error': 'no existe'
        }, status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = Booksr(book)
        return Response(serializer.data)
    if request.method == 'PUT':
        serializer = Booksr(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'DELETE':
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT) """
        
class BookList(APIView):
    def get(self, request):
        books = Book.objects.all()
        serializer=Booksr(books, many=True)
        return Response(serializer.data)

class BookCreate(APIView):
    def post(self, request):
        serializer = Booksr(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class Books(APIView):
    def get_pk(self, pk):
        try: 
            return Book.objects.get(pk=pk)
        except Book.DoesNotExist:
            return None
    def get(self, request, pk):
        book=self.get_pk(pk)
        if not book:
            return Response({
                'error': 'El libro no existe'
            }, status=status.HTTP_404_NOT_FOUND)
        serializer = Booksr(book)
        return Response(serializer.data)
    
    def put(self, request, pk):
        book = self.get_pk(pk)
        serializer = Booksr(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        book=self.get_pk(pk)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)