from django.db import models
from canvas.profile_app.models import Profile


class Product(models.Model):
    TYPES = (
        ('PAINTING', 'Painting'),
        ('PRINT', 'Print'),
        ('PIN', 'Pin'),
        ('STICKERS', 'Stickers'),
        ('DOLL', 'Doll'),
        ('CLOTHING', 'Clothing'),
        ('OTHER', 'Other'),
    )

    PRODUCT_NAME_MAX_LENGTH = 45
    DESCRIPTION_MAX_LENGTH = 250

    product_name = models.CharField(
        max_length=PRODUCT_NAME_MAX_LENGTH,
        blank=False,
        null=False,
    )

    product_description = models.TextField(
        max_length=DESCRIPTION_MAX_LENGTH,
    )

    product_photo = models.ImageField(
        upload_to='product_photos/'
    )

    product_quantity = models.IntegerField()

    product_type = models.CharField(
        choices=TYPES,
        max_length=max(len(x) for (x, _) in TYPES),
    )

    product_price = models.DecimalField(
        max_digits=7,
        decimal_places=2,
    )

    profile = models.ForeignKey(
        Profile, on_delete=models.CASCADE,
    )


class CartItem(models.Model):
    PRODUCT_NAME_MAX_LENGTH = 45
    quantity = models.IntegerField(default=0)
    product_name = models.CharField(
        max_length=PRODUCT_NAME_MAX_LENGTH,
        blank=False,
        null=False,
    )
    product_price = models.DecimalField(
        max_digits=7,
        decimal_places=2,
    )

    profile = models.ForeignKey(Profile, unique=False, on_delete=models.CASCADE)
