from django import forms
from canvas.profile_app.models import PaymentMethod, Address, Profile


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = (
            'username',
            'profile_photo',
            'description',
            'country'
        )
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
            'profile_photo': forms.FileInput(attrs={'class': 'form-control'})
        }


class EditBannerForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = (
            'shop_banner',
        )
        widgets = {
            'shop_banner': forms.FileInput(attrs={'class': 'form-control'}),
        }


class AddPaymentForm(forms.ModelForm):
    class Meta:
        model = PaymentMethod
        fields = ('card_number', 'card_expiry', 'card_cvv')
        labels = {
            'card_number': 'Enter card number',
            'card_expiry': 'Enter expiration date',
            'card_cvv': 'Enter the security code (CVV/CVC)'
        }


class EditPaymentForm(forms.ModelForm):
    class Meta:
        model = PaymentMethod
        fields = ('card_expiry',)
        labels = {
            'card_expiry': 'Enter the new expiration date',
        }


class DeletePaymentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
            field.required = False

    class Meta:
        model = PaymentMethod
        exclude = ('card_number', 'card_expiry', 'card_cvv', 'profile')


class AddAddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ('country', 'city', 'details')
        labels = {
            'details': 'Enter street name and number',
        }


class EditAddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ('country', 'city', 'details',)
        labels = {
            'details': 'Enter street name and number:',
        }


class DeleteAddressForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
            field.required = False

    class Meta:
        model = Address
        exclude = ('country', 'city', 'details', 'primary', 'profile')


