# Generated by Django 4.0.3 on 2022-03-27 12:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('profile_app', '0003_address_primary_alter_address_country'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=45)),
                ('product_description', models.TextField(max_length=250)),
                ('product_photo', models.ImageField(upload_to='')),
                ('product_quantity', models.IntegerField()),
                ('product_type', models.CharField(choices=[('PAINTING', 'Painting'), ('PRINT', 'Print'), ('PIN', 'Pin'), ('STICKERS', 'Stickers'), ('DOLL', 'Doll'), ('CLOTHING', 'Clothing'), ('OTHER', 'Other')], max_length=8)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profile_app.profile')),
            ],
        ),
    ]