from canvas.main.models import Product
from canvas.profile_app.models import PaymentMethod, Profile


def get_payment_methods(pk):
    payment_methods = PaymentMethod.objects.filter(profile_id=pk)
    return payment_methods


def get_profile_by_username(username):
    return Profile.objects.filter(username=username)[0]


def get_products_by_profile_username(username):
    profile = Profile.objects.filter(username=username)[0]
    return Product.objects.filter(profile=profile)