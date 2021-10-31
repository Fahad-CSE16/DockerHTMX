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
# Aggregation

```
prod_avg_agg = Product.objects.aggregate(Avg('price'), Max('price'), Min('price'))
print("Aggegate=",prod_avg_agg['price__min'],prod_avg_agg['price__max'],prod_avg_agg['price__avg'])
```

it will return calculated output of all objects. But Generating aggregates for each item in a QuerySet can be done by by annotate.
Per-object summaries can be generated using the annotate() clause. When an annotate() clause is specified, each object in the QuerySet will be annotated with the specified values.
 For example, if you are retrieving a list of Priducts, you may want to know how many users  liked to each product. Each product has a many-to-many relationship with the users; we want to summarize this relationship for each product in the QuerySet.
 
## Talk about Annotate

``` 
ann= Product.objects.annotate(new=Sum('price'))
```

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

# lambda Function
basic Syntax = 
```
labda perameters : experession
```
```
a = lambda a,b : a*a + 2*a*b + b*b
```

# calling lambda with perameters
```
a = (lambda a,b : a*a + 2*a*b + b*b)(2,3)
```


# map functions basic syntax
```
b= map(functionname, list_variable)
``` 
example 
```
b= map( lambda a: a*a  , [3,4] )
```
It will return map object.. To get values make it as list
`print(list(b))`

# Comprehensive 
```
num=[3,4,5]
comprehensive= [ x*x for x in num]
```

# For Filtering in comprehensive list 
```
filtered= [x for x in range(1,11) if x%2==0]
```
# swap variable value
```
a, b= 5, 10
a,b = b, a
```


