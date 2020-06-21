from django.shortcuts import render
from rest_framework import routers, serializers, viewsets, status
from rest_framework.response import Response
from django.contrib.auth.models import User
from .serializer import UserSerializer,AuthorSerializer,BookSerializer
from .models import Author, Book
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializers_class = UserSerializer

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class BookViewSet(viewsets.ModelViewSet):
    permission_class = (IsAuthenticated)
    queryset = Book.objects.all()
    serializer_class =  BookSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fiels = ['release_date']