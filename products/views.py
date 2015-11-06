from django.shortcuts import render

# Create your views here.

def all_products(request):
    return render(request, 'all_products.html')

def product(request, product_id):
    return render(request, 'product.html')

def index(request):
    return render(request, 'index.html')
