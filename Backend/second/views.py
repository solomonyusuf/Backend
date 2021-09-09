from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from .serializers import SecondContactSerializer, SecondNewsSerializer
from .models import Contact, News


class SecondContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = SecondContactSerializer

class SecondNewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = SecondNewsSerializer