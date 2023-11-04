from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status  # Import status module

from .Serializer import *  # Use the correct import path
from .models import Book

# Create your views here.
# get
@api_view(['GET'])
def Booklist(request):
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)  # Serialize a queryset
    return Response(serializer.data)

# post
@api_view(['POST'])
def postBooklist(request):
    books = Book.objects.all()
    serializer = BookSerializer(data=request.data)  # Serialize a queryset
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

# update
@api_view(['POST'])
def updateBooklist(request,id):
    books = Book.objects.get(id=id)
    serializer = BookSerializer(instance=books,data=request.data)  # Serialize a queryset
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def deleteBooklist(request,id):
    books = Book.objects.get(id=id)
    books.delete();
    return Response('deleted succesfully')

# @api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
# def demo(request, pk):
#     try:
#         book = Book.objects.get(pk=pk)
#     except Book.DoesNotExist:
#         return Response({'error': 'Book not found'}, status=status.HTTP_404_NOT_FOUND)
#
#     if request.method == 'GET':
#         serializer = BookSerializer(book)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#     elif request.method in ['PUT', 'PATCH']:
#         serializer = BookSerializer(book, data=request.data, partial=True if request.method == 'PATCH' else False)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     elif request.method == 'DELETE':
#         book.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
