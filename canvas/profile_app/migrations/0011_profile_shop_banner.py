# Generated by Django 4.0.3 on 2022-04-06 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile_app', '0010_remove_paymentmethod_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='shop_banner',
            field=models.ImageField(default=1, upload_to='banner_photos/'),
            preserve_default=False,
        ),
    ]