from django.shortcuts import render
from models import Product

# Create your views here.

def all_products(request):
    results = Product.objects.all()
    return render(request, 'all_products.html', {'results':results})

def product(request, product_id):
    product = Product.objects.get(pk=product_id)
    return render(request, 'product.html', {'product':product})

def index(request):
    return render(request, 'index.html')
