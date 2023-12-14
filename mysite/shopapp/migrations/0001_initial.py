# Generated by Django 5.0 on 2023-12-14 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Название товара', max_length=255, verbose_name='Название')),
                ('descriptoin', models.TextField(help_text='Описание товара', verbose_name='Описание')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена')),
                ('stock_quantity', models.SmallIntegerField(verbose_name='Остаток на складе')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='Дата последнего изменения')),
                ('publised', models.BooleanField(default=False, help_text='True - опубликовано, False - черновик', verbose_name='Опубликовано')),
            ],
        ),
    ]
