# Generated by Django 3.0.8 on 2020-08-21 01:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
        ('product', '0001_initial'),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='item',
            field=models.ManyToManyField(related_name='order_item', through='order.Order', to='product.Product'),
        ),
    ]
