from django.contrib import admin

# Register your models here.
from canvas.profile_app.models import Address, PaymentMethod, Profile


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    pass


@admin.register(PaymentMethod)
class PaymentMethodAdmin(admin.ModelAdmin):
    pass


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("username", "user")
