from canvas.main.models import CartItem
from canvas.profile_app.models import PaymentMethod, Address


def get_cart_items(current_profile):
    return CartItem.objects.filter(profile=current_profile)


def get_total_price(current_profile):
    total = 0
    cart_items = get_cart_items(current_profile)
    for item in cart_items:
        total += item.product.product_price * item.quantity
    return total


def get_available_payment_methods(current_profile):
    return PaymentMethod.objects.filter(profile=current_profile)


def get_available_addresses(current_profile):
    return Address.objects.filter(profile=current_profile)
