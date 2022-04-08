from django.test import TestCase

from canvas.auth_app.models import CanvasUser
from canvas.main.models import Product
from canvas.profile_app.helpers import get_payment_methods, get_products_by_profile_username
from canvas.profile_app.models import Profile, PaymentMethod


class TestHelpersReturnCorrectValues(TestCase):
    def setUp(self):
        user = CanvasUser.objects.create(email='mo@abv.bg')
        profile = Profile.objects.create(username='mo', profile_photo='../../../static/images/logo.png', user=user)
        card1 = PaymentMethod.objects.create(card_number='4532297793563207', card_expiry='12/23', card_cvv='123',
                                             profile=profile)
        card2 = PaymentMethod.objects.create(card_number='5423241374319083', card_expiry='12/23', card_cvv='123',
                                             profile=profile)
        prod1 = Product.objects.create(product_name='name', product_photo='../../../static/images/logo.png',
                                       product_price=1.00, product_quantity=1, product_description='description',
                                       profile=profile)
        prod1 = Product.objects.create(product_name='name2', product_photo='../../../static/images/logo.png',
                                       product_price=1.00, product_quantity=1, product_description='description',
                                       profile=profile)

    def test_get_payment_method_returns_correct_list_of_cards(self):
        payment_methods = get_payment_methods(1)
        self.assertEqual(str(payment_methods[1]), str(PaymentMethod.objects.all()[1]))

    def test_get_products_returns_correct_product_set(self):
        products = get_products_by_profile_username('mo')
        self.assertEqual(products[0], Product.objects.all()[0])
