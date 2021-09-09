from django.urls import include, path
from rest_framework import routers
from . import views


router = routers.DefaultRouter()
router.register(r'Second/api/contact', views.SecondContactViewSet)
router.register(r'Second/api/news', views.SecondNewsViewSet)

urlpatterns=[
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    
    
    ]
