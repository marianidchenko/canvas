from django.contrib import admin

# Register your models here.
from canvas.main.models import Product, CartItem


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass


@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    pass

