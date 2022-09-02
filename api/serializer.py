from rest_framework import serializers
from api.models import Productmodel

#create serializers here
class ProductSerializer(serializers.HyperlinkedModelSerializer):
    id=serializers.ReadOnlyField()
    class Meta:
        model=Productmodel
        fields=[
            "id","product","catagory","price","discription"
        ]