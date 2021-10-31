from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=100)

class Product(models.Model):
    cate=models.ForeignKey(Category, on_delete=models.CASCADE)
    user= models.ForeignKey(User, on_delete=models.CASCADE)

    name = models.CharField(max_length=100)
    price= models.IntegerField()




