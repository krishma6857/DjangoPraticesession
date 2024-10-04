from django.shortcuts import render
from .models import Products


# Create your views here.

def home(req):
    context = {}
    products = Products.objects.all()
    context ['t'] = products
    print(len(products))
    return render(req,'shop/home.html',context)