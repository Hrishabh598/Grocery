# Generated by Django 4.2.1 on 2023-07-12 13:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Groceryapp', '0006_cart_cartitem'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='user',
        ),
        migrations.RemoveField(
            model_name='cartitem',
            name='cart',
        ),
        migrations.RemoveField(
            model_name='cartitem',
            name='item',
        ),
        migrations.DeleteModel(
            name='Orders',
        ),
        migrations.DeleteModel(
            name='Cart',
        ),
        migrations.DeleteModel(
            name='cartItem',
        ),
    ]