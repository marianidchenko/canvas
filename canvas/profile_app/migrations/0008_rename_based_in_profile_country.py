# Generated by Django 4.0.3 on 2022-04-05 17:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profile_app', '0007_profile_based_in'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='based_in',
            new_name='country',
        ),
    ]
