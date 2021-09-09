from django.urls import include, path
from rest_framework import routers
from . import views


router = routers.DefaultRouter()
router.register(r'Third/api/contact', views.ThirdContactViewSet)
router.register(r'Third/api/news', views.ThirdNewsViewSet)

urlpatterns=[
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    
    
    ]
