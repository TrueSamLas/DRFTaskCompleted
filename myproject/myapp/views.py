from django.shortcuts import render
from rest_framework import generics
from .models import Books
from .serializers import BooksSerializers


class BooksList(generics.ListCreateAPIView):
    queryset = Books.objects.all()
    serializer_class = BooksSerializers


class BooksDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Books.objects.all()
    serializer_class = BooksSerializers
