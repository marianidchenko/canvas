from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse_lazy, reverse

from canvas.main.models import Product, CartItem
from canvas.profile_app.models import Profile, PaymentMethod

UserModel = get_user_model()


class TestViews(TestCase):
    def setUp(self):
        self.user = UserModel.objects.create_user(email='mo@abv.bg', password='password')
        self.profile = Profile.objects.create(username='mo', profile_photo='../../../static/images/logo.png',
                                              user=self.user)
        self.user.profile = self.profile
        self.card1 = PaymentMethod.objects.create(card_number='4532297793563207', card_expiry='12/23', card_cvv='123',
                                                  profile=self.profile)
        self.card2 = PaymentMethod.objects.create(card_number='5423241374319083', card_expiry='12/23', card_cvv='123',
                                                  profile=self.profile)
        self.prod1 = Product.objects.create(product_name='name', product_photo='../../../static/images/logo.png',
                                            product_price=1.00, product_quantity=1, product_description='description',
                                            profile=self.profile)
        self.prod2 = Product.objects.create(product_name='name2', product_photo='../../../static/images/logo.png',
                                            product_price=1.00, product_quantity=2, product_description='description',
                                            profile=self.profile)
        CartItem.objects.create(quantity=1, product=self.prod1, profile=self.profile)

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

    def test_correct_queryset_on_browser(self):
        response = self.client.get(reverse_lazy('browse'))
        self.assertQuerysetEqual(response.context_data['products'], [self.prod2, self.prod1])

    def test_correct_profile_queryset_on_profile_products_view(self):
        response = self.client.get(reverse_lazy('profile products', kwargs={'username': 'mo'}))
        self.assertQuerysetEqual(list(response.context_data['products']), [self.prod1, self.prod2])

    def test_correct_profile_queryset_on_profile_details_view(self):
        response = self.client.get(reverse_lazy('profile details', kwargs={'username': 'mo'}))
        self.assertQuerysetEqual(list(response.context_data['products']), [self.prod1, self.prod2])

    def test_correct_profile_queryset_on_manage_products_view(self):
        self.client.login(email='mo@abv.bg', password='password')
        response = self.client.get(reverse_lazy('manage products'))
        self.assertQuerysetEqual(list(response.context_data['products']), [self.prod1, self.prod2])

