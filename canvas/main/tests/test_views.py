from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse_lazy, reverse

from canvas.main.models import Product, CartItem
from canvas.profile_app.models import Profile, PaymentMethod

UserModel = get_user_model()


class TestViews(TestCase):
    def setUp(self):
        user = UserModel.objects.create_user(email='mo@abv.bg', password='password')
        profile = Profile.objects.create(username='mo', profile_photo='../../../static/images/logo.png', user=user)
        card1 = PaymentMethod.objects.create(card_number='4532297793563207', card_expiry='12/23', card_cvv='123',
                                             profile=profile)
        card2 = PaymentMethod.objects.create(card_number='5423241374319083', card_expiry='12/23', card_cvv='123',
                                             profile=profile)
        prod1 = Product.objects.create(product_name='name', product_photo='../../../static/images/logo.png',
                                       product_price=1.00, product_quantity=1, product_description='description',
                                       profile=profile)
        prod2 = Product.objects.create(product_name='name2', product_photo='../../../static/images/logo.png',
                                       product_price=1.00, product_quantity=1, product_description='description',
                                       profile=profile)
        CartItem.objects.create(quantity=1, profile=profile, product=prod1)


    def test_correct_context_data_on_index_page(self):
        response = self.client.get(reverse_lazy('index'))
        self.assertEqual(
            'Welcome to Canvas',
            response.context_data['title']
        )

    def test_correct_context_data_on_cart_page(self):
        user = UserModel.objects.all().first()
        user.profile = Profile.objects.all()[0]
        user.save()
        self.client.login(email='mo@abv.bg', password='password')
        response = self.client.get(reverse('cart'))
        self.assertEqual(
            1.00,
            response.context_data['total']
        )

    def test_correct_context_data_on_checkout_page(self):
        user = UserModel.objects.all().first()
        user.profile = Profile.objects.all()[0]
        user.save()
        self.client.login(email='mo@abv.bg', password='password')
        response = self.client.get(reverse('checkout'))
        self.assertEqual(
            response.context_data['items'][0],
            CartItem.objects.all().first()
        )