from django.contrib.auth.models import User
import random
from .models import Category, Product
from lorem_text import lorem

def addProd():
    for i in range(400): 
        Product.objects.create(name=lorem.words(2),
        cate=Category.objects.get(id=random.randint(1, 3)),
        user=User.objects.get(id=random.randint(1, 3)),
        price=random.randrange(100, 100000, 1))
    return None