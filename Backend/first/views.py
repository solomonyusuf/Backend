from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from .serializers import FirstContactSerializer, FirstNewsSerializer
from .models import Contact, News


class FirstContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = FirstContactSerializer

class FirstNewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = FirstNewsSerializer