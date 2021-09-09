from django.db import models

# Create your models here.
class Contact(models.Model):
    fullname= models.CharField(max_length=225)
    phoneNumber= models.CharField(max_length=225)
    email= models.CharField(max_length=225)
    message=models.CharField(max_length=225)

class News(models.Model):
    image=models.FileField()
    title=models.CharField(max_length=225)
    body=models.CharField(max_length=2000)
    date=models.DateTimeField()



    