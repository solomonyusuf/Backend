from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from .serializers import ThirdContactSerializer, ThirdNewsSerializer
from .models import Contact, News


class ThirdContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ThirdContactSerializer

class ThirdNewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = ThirdNewsSerializer