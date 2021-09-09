from rest_framework import serializers

from .models import Contact, News

class ThirdContactSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Contact
        fields = ('id','fullname', 'phoneNumber','email','message')

class ThirdNewsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = News
        fields = ('id','image', 'title','body','date')
