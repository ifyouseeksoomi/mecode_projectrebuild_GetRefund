# Generated by Django 3.0.8 on 2020-08-21 01:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0001_initial'),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=50)),
            ],
            options={
                'db_table': 'order_statuses',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('order_status', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='order.OrderStatus')),
                ('product', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='product.Product')),
                ('user', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='user.User')),
            ],
            options={
                'db_table': 'orders',
            },
        ),
    ]
