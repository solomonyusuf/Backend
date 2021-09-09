from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from .serializers import ContactSerializer, NewsSerializer
from .models import Contact, News


class TripplegContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

class TripplegNewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer