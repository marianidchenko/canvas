# Generated by Django 4.0.3 on 2022-04-13 10:33

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_rename_crated_on_product_created_on'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_photo',
            field=cloudinary.models.CloudinaryField(max_length=255),
        ),
    ]
