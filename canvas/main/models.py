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

    product_photo = models.ImageField()

    product_quantity = models.IntegerField()

    product_type = models.CharField(
        choices=TYPES,
        max_length=max(len(x) for (x, _) in TYPES),
    )

    @property
    def out_of_stock(self):
        if self.product_quantity == 0:
            return True
        else:
            return False

    owner = models.ForeignKey(Profile, on_delete=models.CASCADE)




