# Generated by Django 4.2.5 on 2023-11-24 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0003_cart_size'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='size',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='product',
            name='base_price',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='product',
            name='quantity',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='product',
            name='sale_price',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='product',
            name='sizes',
            field=models.PositiveIntegerField(choices=[(5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10')], default=0),
        ),
    ]