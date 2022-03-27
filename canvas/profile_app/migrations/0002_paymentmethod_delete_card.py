# Generated by Django 4.0.3 on 2022-03-22 12:01

import creditcards.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profile_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentMethod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_number', creditcards.models.CardNumberField(max_length=25)),
                ('card_expiry', creditcards.models.CardExpiryField()),
                ('card_cvv', creditcards.models.SecurityCodeField(max_length=4)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profile_app.profile')),
            ],
        ),
        migrations.DeleteModel(
            name='Card',
        ),
    ]