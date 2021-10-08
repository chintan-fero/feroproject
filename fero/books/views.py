from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework import status
from books.models import Book
from books.serializers import BookSerializer
from django.http import HttpResponse, JsonResponse

@csrf_exempt
def book_list(request):
    if request.method == 'GET':
        books = Book.objects.all()
        book_serializer = BookSerializer(books, many=True)
        return JSONResponse(book_serializer.data)
    elif request.method == 'POST':
        book_data = JSONParser().parse(request)
        book_serializer = BookSerializer(data=book_data)
        if book_serializer.is_valid():
            book_serializer.save()
            return JSONResponse(book_serializer.data,status=status.HTTP_201_CREATED)
        return JSONResponse(book_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
def book_detail(request, pk):
    try:
        book = Book.objects.get(pk=pk)
    except book.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)
        if request.method == 'GET':
            book_serializer = BookSerializer(book)
            return JSONResponse(book_serializer.data)
        elif request.method == 'PUT':
            book_data = JSONParser().parse(request)
            book_serializer = BookSerializer(book, data=book_data)
            if book_serializer.is_valid():
                book_serializer.save()
                return JSONResponse(book_serializer.data)
            return JSONResponse(book_serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        elif request.method == 'DELETE':
            book.delete()
            return HttpResponse(status=status.HTTP_204_NO_CONTENT)
