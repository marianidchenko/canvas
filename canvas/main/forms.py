import self
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
        return f'{obj.get_country_display()}, {obj.city}, {obj.details}'


class Card:
    pass


class ChooseCardAndAddress(forms.Form):
    def __init__(self, profile, *args, **kwargs):
        super(ChooseCardAndAddress, self).__init__(*args, **kwargs)
        self.fields['card'].queryset = PaymentMethod.objects.filter(profile=profile.pk)
        self.fields['address'].queryset = Address.objects.filter(profile=profile.pk)

    card = CardChoiceField(queryset=None)
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