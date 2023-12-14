from django.shortcuts import render
from .models import Product, Order


def index(request):
    return render(request, 'index.html')


def products(request):
    list_products = Product.objects.filter(published=True)
    return render(request, 'products.html', {'products': list_products})


def orders(request):
    list_orders = Order.objects.all()
    return render(request, 'orders.html', {'orders': list_orders})
