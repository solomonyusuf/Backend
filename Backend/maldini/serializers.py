from rest_framework import serializers

from .models import Contact, News, Products

class MaldiniContactSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Contact
        fields = ('id','fullname', 'phoneNumber','email','message')

class MaldiniNewsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = News
        fields = ('id','image', 'title','body','date')

class MaldiniProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Products
        fields = ('id','image', 'name','description','date')
