from django.db import models

# Create your models here.
class Productmodel(models.Model):
    product=models.CharField(max_length=90)
    catagory=models.CharField(max_length=90)
    discription=models.TextField()
    price=models.DecimalField(max_digits=9,decimal_places=2)

