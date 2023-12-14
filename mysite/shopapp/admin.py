from django.contrib import admin
from .models import Product, Order


@admin.register(Product)
class ProductkAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price', 'stock_quantity', 'update_time', 'published']
    list_display_links = ['id', 'name']
    list_filter = ['name', 'update_time', 'published']
    search_fields = ['name']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'client', 'update_time']
    list_display_links = ['id', 'client', 'update_time']
    list_filter = ['client', 'update_time']
    search_fields = ['client', 'update_time']
