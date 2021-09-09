from django.shortcuts import render
from rest_framework import viewsets
# Create your views here.


from .serializers import MaldiniContactSerializer, MaldiniNewsSerializer, MaldiniProductSerializer
from .models import Contact, News, Products


class MaldiniContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = MaldiniContactSerializer

class MaldiniNewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = MaldiniNewsSerializer

class MaldiniProductsViewSet(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = MaldiniProductSerializer

class MarbleViewSet(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = MaldiniProductSerializer

class GraniteViewSet(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = MaldiniProductSerializer

