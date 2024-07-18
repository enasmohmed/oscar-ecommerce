# Generated by Django 2.2.13 on 2021-11-20 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0009_auto_20211120_2018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_status',
            field=models.CharField(choices=[('Order Placed', 'Order Placed'), ('Order Processing', 'Order Processing'), ('Shipped', 'Shipped'), ('Delivered', 'Delivered')], default='Order Processing', max_length=100),
        ),
    ]