from django.shortcuts import render
from models import Product
from rest_framework import generics
from serializers import ProductSerializer

# Create your views here.

def all_products(request):
    results = Product.objects.all()
    return render(request, 'all_products.html', {'results':results})

class productInfo(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

def product(request, product_id):
    product = Product.objects.get(pk=product_id)
    return render(request, 'product.html', {'product':product})

def index(request):
    return render(request, 'index.html')


