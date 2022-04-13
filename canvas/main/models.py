from cloudinary.models import CloudinaryField
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
    PRODUCT_QUANTITY_MIN = 0

    product_name = models.CharField(
        max_length=PRODUCT_NAME_MAX_LENGTH,
        blank=False,
        null=False,
    )

    product_description = models.TextField(
        max_length=DESCRIPTION_MAX_LENGTH,
    )

    product_photo = CloudinaryField(
        overwrite=True,
        resource_type="image",
        transformation={"quality": "auto:eco"},
        format="jpg",
    )

    product_quantity = models.PositiveIntegerField()

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

    created_on = models.DateTimeField(
        auto_now_add=True,
    )


class CartItem(models.Model):
    quantity = models.IntegerField(default=0)
    product = models.ForeignKey(Product, unique=False, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, unique=False, on_delete=models.CASCADE)
