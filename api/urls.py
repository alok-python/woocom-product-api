from django.contrib import admin
from django.urls import path,include
from api.views import ProductViewSet
from rest_framework import routers


router= routers.DefaultRouter()
router.register(r'',ProductViewSet)


urlpatterns = [    
    path('product/',include(router.urls)),
    
]
