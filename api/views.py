from django.shortcuts import render
from rest_framework import viewsets
from api.models import Productmodel
from api.serializer import ProductSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.


def apidocumentation(request):
    return render(request,'index.html')


class ProductViewSet(viewsets.ModelViewSet):
    queryset= Productmodel.objects.all()
    serializer_class=ProductSerializer


