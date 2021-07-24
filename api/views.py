from django.shortcuts import render
from .models import *
from rest_framework import status 
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *

# Create your views here.
@api_view(['GET'])
def book_list(request):
	#list all books 
	if request.method == 'GET':
		books = Book.objects.all()
		serializer = BookSerializer(books, many=True)
		return Response(serializer.data)



@api_view(['GET'])
def book_detail(requst, id):
	book = Book.objects.get(id=id)
	serializer = BookSerializer(book,many=False)
	return Response(serializer.data)


@api_view(['POST'])
def add_book(request, id):
	serializer = BookSerializer(data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)




@api_view(['POST'])
def update_book(request, id):
	book = Book.objects.get(id=id)
	serializer = BookSerializer(instance=book, data=request.data)

	if serializer.is_valid():
		serializer.save()
	return Response(serializer.data)



@api_view(['DELETE'])
def delete_book(request, id):
	book = Book.objects.get(id=id)
	book.delete()

	return Response('Deleted')