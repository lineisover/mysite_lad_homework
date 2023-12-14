from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    name = models.CharField(max_length=255,
                            verbose_name='Название',
                            help_text='Название товара')
    descriptoin = models.TextField(verbose_name='Описание',
                                   help_text='Описание товара')
    price = models.DecimalField(verbose_name='Цена', decimal_places=2, max_digits=10)
    stock_quantity = models.SmallIntegerField(verbose_name='Остаток на складе')
    update_time = models.DateTimeField(verbose_name='Дата последнего изменения',
                                       auto_now=True)
    publised = models.BooleanField(verbose_name='Опубликовано',
                                   help_text='True - опубликовано, False - черновик',
                                   default=False)


class Order(models.Model):
    comment = models.TextField(verbose_name='Комментарий')
    promo = models.CharField(max_length=20,
                             verbose_name='Промокод',
                             blank=True)
    update_time = models.DateTimeField(verbose_name='Дата последнего изменения заказа',
                                       auto_now=True)
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
