from django import forms

from canvas.main.models import Product


class CreateProductFrom(forms.ModelForm):
    class Meta:
        model = Product
        fields = (
            'product_name',
            'product_description',
            'product_photo',
            'product_quantity',
            'product_price',
            'product_type'
        )
