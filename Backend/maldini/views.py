from django.shortcuts import render
from rest_framework import viewsets
# Create your views here.


from .serializers import MaldiniContactSerializer, MaldiniNewsSerializer, MaldiniOrdersSerializer,MaldiniProductSerializer
from .models import Contact, News, Products,Orders


class MaldiniContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = MaldiniContactSerializer

class MaldiniNewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = MaldiniNewsSerializer

class MaldiniProductsViewSet(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = MaldiniProductSerializer

class MaldiniOrdersViewSet(viewsets.ModelViewSet):
    queryset = Orders.objects.all()
    serializer_class = MaldiniOrdersSerializer

class MarbleViewSet(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = MaldiniProductSerializer

class GraniteViewSet(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = MaldiniProductSerializer

