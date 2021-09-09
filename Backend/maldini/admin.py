from django.contrib import admin
from .models import Contact, News, Products
# Register your models here.
admin.site.register(Contact)
admin.site.register(News)
admin.site.register(Products)