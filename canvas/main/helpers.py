from canvas.main.models import CartItem
from canvas.profile_app.models import PaymentMethod, Address


def get_total_cart_price(current_profile):
    total_price = 0
    for cartitem in CartItem.objects.filter(profile=current_profile):
        total_price += cartitem.product.product_price * cartitem.quantity
    return total_price


def get_available_payment_methods(current_profile):
    return PaymentMethod.objects.filter(profile=current_profile)


def get_available_addresses(current_profile):
    return Address.objects.filter(profile=current_profile)
