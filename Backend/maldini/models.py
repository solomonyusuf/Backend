from django.db import models

# Create your models here.
class Contact(models.Model):
    fullname= models.CharField(max_length=225)
    phoneNumber= models.CharField(max_length=225)
    email= models.CharField(max_length=225)
    message=models.CharField(max_length=225)

class News(models.Model):
    image=models.ImageField(null=True)
    title=models.CharField(max_length=225)
    body=models.CharField(max_length=2000)
    date=models.DateTimeField()

class Products(models.Model):
    image=models.ImageField(null=True)
    name=models.CharField(max_length=225)
    description=models.CharField(max_length=2000)
    date=models.DateTimeField()
    productcode=models.CharField(null=True, max_length=225)
   