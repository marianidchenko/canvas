# Generated by Django 4.0.3 on 2022-04-07 12:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_product_crated_on'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='crated_on',
            new_name='created_on',
        ),
    ]