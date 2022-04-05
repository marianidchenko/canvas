from django import forms
from canvas.main.models import Product
from canvas.profile_app.models import PaymentMethod, Address


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
        widgets = {
            'product_description': forms.Textarea(attrs={'rows': 3}),
            'product_photo': forms.FileInput(attrs={'class': 'form-control'}),
        }


class CardChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return f'**** **** **** {obj.card_number[-4:]}'


class AddressChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        country = [c for c in obj.COUNTRIES if obj.country in c][0][1]
        return f'{country}, {obj.city}, {obj.details}'


class ChooseCardAndAddress(forms.Form):
    card = CardChoiceField(queryset=PaymentMethod.objects.all())
    address = AddressChoiceField(queryset=Address.objects.all())


class ProductEditForm(forms.ModelForm):
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
        widgets = {
            'product_description': forms.Textarea(attrs={'rows': 3}),
            'product_photo': forms.FileInput(attrs={'class': 'form-control'}),
        }


class ProductRestockForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = (
            'product_quantity',
        )


class ProductDeleteForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = (
            'product_name',
            'product_description',
            'product_photo',
            'product_quantity',
            'product_price',
            'product_type',
            'profile'
        )