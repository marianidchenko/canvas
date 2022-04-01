from django.contrib import admin

# Register your models here.
from canvas.main.models import Product, CartItem


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("product_name", "product_description", "product_quantity", "profile")
    search_fields = ("product_name",)
    fields = ("product_name", "product_description", "product_photo")


@admin.register(CartItem)
class CartItem(admin.ModelAdmin):
    pass
