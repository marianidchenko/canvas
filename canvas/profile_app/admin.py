from django.contrib import admin

# Register your models here.
from canvas.profile_app.models import Address, PaymentMethod


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    pass


@admin.register(PaymentMethod)
class PaymentMethodAdmin(admin.ModelAdmin):
    pass



