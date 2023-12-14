from django.urls import path
from . import views


urlpatterns = [
    path('orders/', views.orders, name='orders'),
    path('products/', views.products, name='products'),
    path('', views.index, name='home'),
]
