# Generated by Django 5.2.3 on 2025-06-13 01:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('e_shop', '0002_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to='images'),
        ),
    ]
