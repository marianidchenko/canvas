# Generated by Django 4.0.3 on 2022-04-06 14:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profile_app', '0009_paymentmethod_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='paymentmethod',
            name='type',
        ),
    ]