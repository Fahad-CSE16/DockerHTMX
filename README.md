```
docker-compose build
docker-compose up
```


```

from django.db.models import Avg,Count,Min,Max, 

def TryAll(request):
    prod_avg_agg = Product.objects.aggregate(Avg('price'), Max('price'), Min('price'))
    print("Aggegate=",prod_avg_agg['price__min'],prod_avg_agg['price__max'],prod_avg_agg['price__avg'])
    
    # Minimum required structure for group
    pubs = Product.objects.values('cate').annotate(num_category=Max('price'))

    # pubs = Product.objects.values('price').annotate(num_category=Count('price', filter=Q(price__lte=5000)))
    # pubs = Product.objects.annotate(num_category=Min('price')).order_by('num_category')
    pubs = Product.objects.values('cate').order_by().annotate(num_category=Max('price'))
    for i in pubs:
        print(pubs.count())
        print("Annonate=",i)


```

## Talk about Annotate

``` 
ann= Product.objects.annotate(new=Sum('price'))
``

In this case it will add a new field named `new` with each objects of product model and its value will be Sum of That object price only. Because annotate not found any groups and thus he assumes each object as a group. In this case it returns a queryset.
But if 
```
ann= Product.objects.annotate(new=Count('likes'))
```
where likes is a MAny to many field or an arrayfiled , then it will count number of objects related to this field..

```
ann= Product.objects.values('category').annotate(new=Sum('price'))
```

In this case it returns a list od Dict Object. In this case it will make groups for each category and  add a new field named `new` with each groups (dict obj) like `[{'category': 3, 'new': 6638652}, {'category': 1, 'new': 6737454}, {'category': 2, 'new': 7128912}]`  and its value will be Sum of That groups object price only. 
If we add extra filed with `values()` like `values('category', 'user')` then it will make groups my making combination of these fields.

Then there comes possibility to order groups like
```
ann= Product.objects.values('category').annotate(new=Sum('price')).order_by('new')
```
By doing this, groups(not objects) will be  ordered according to values of new. If we want to sort according to `category_id` then we have to use `.values('category')`


if we are clear about these concepts then we can use multiplate annotate in same like using same process.
Happy coding!


