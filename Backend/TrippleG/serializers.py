from rest_framework import serializers

from .models import Contact, News

class ContactSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Contact
        fields = ('id','fullname', 'phoneNumber','email','message')

class NewsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = News
        fields = ('id','image', 'title','body','date')
