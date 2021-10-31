from django.db.models.aggregates import Sum
from django.shortcuts import render
from django.db.models import Avg,Count,Min,Max, Q
# Create your views here.
from .models import Product
from django.shortcuts import HttpResponse

def TryAll(request):
    prod_avg_agg = Product.objects.aggregate(Avg('price'), Max('price'), Min('price'))
    print("Aggegate=",prod_avg_agg['price__min'],prod_avg_agg['price__max'],prod_avg_agg['price__avg'])



    # pubs = Product.objects.values('price').annotate(num_category=Count('price', filter=Q(price__lte=5000)))
    # pubs = Product.objects.annotate(num_category=Min('price')).order_by('price')
    pubs = Product.objects.values('cate').annotate(num_category=Sum('price')).order_by('num_category')
    # pubs= Product.objects.annotate(fahad=Sum('price')).order_by('fahad')
    print(pubs)
    for i in pubs:
        print(pubs.count())
        print("Annonate=",i['num_category'])












    return HttpResponse(prod_avg_agg['price__min'])
