# Generated by Django 4.0.3 on 2022-04-05 17:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profile_app', '0005_profile_descriptions'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='descriptions',
            new_name='description',
        ),
    ]
