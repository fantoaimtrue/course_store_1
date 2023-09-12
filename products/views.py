from django.shortcuts import render
from products.models import Product, ProductCategory


def index(request):
    context = {
        'title': 'Store',
        'username': 'Alexandr',
    }
    return render(request, 'products/index.html', context)


def products(requests):
    context = {
        'title': 'Store - Каталог',
        'products': Product.objects.all(),
        'categories': ProductCategory.objects.all()
    }
    return render(requests, 'products/products.html', context)

