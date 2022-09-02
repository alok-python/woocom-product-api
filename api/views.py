from rest_framework import viewsets
from api.models import Productmodel
from api.serializer import ProductSerializer
# Create your views here.




class ProductViewSet(viewsets.ModelViewSet):
    queryset= Productmodel.objects.all()
    serializer_class=ProductSerializer


