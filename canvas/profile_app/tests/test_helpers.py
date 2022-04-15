from django.test import TestCase

from canvas.auth_app.models import CanvasUser
from canvas.main.models import Product
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

