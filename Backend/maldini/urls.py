from django.urls import include, path
from rest_framework import routers
from . import views


router = routers.DefaultRouter()
router.register(r'maldini/api/contact', views.MaldiniContactViewSet)
router.register(r'maldini/api/news', views.MaldiniNewsViewSet)
router.register(r'maldini/api/products', views.MaldiniProductsViewSet)

urlpatterns=[
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    
    
    ]
