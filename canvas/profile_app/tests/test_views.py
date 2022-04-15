from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from canvas.profile_app.models import *

UserModel = get_user_model()


class ProfileDetailsViewTest(TestCase):
    def setUp(self):
        self.user = UserModel.objects.create_user(email='mo@abv.bg', password='password')
        self.profile = Profile.objects.create(username='mo', profile_photo='../../../static/images/logo.png',
                                              user=self.user)
        self.user.profile = self.profile
        self.card1 = PaymentMethod.objects.create(card_number='4532297793563207', card_expiry='12/23', card_cvv='123',
                                                  profile=self.profile)
        self.card2 = PaymentMethod.objects.create(card_number='5423241374319083', card_expiry='12/23', card_cvv='123',
                                                  profile=self.profile)
        self.address1 = Address.objects.create(country='AL', city='City', details='Details', profile=self.profile)

    def test_view_returns_correct_profile_for_queryset(self):
        self.client.post(
            reverse('profile details', kwargs={'username': 'mo'})
        )
        self.assertTemplateUsed('profile/profile_detail.html')

    def test_context_data_is_correct_on_manage_payments_view(self):
        self.client.login(email='mo@abv.bg', password='password')
        response = self.client.get(reverse('manage payments', kwargs={'username': 'mo'}))
        self.assertQuerysetEqual(list(response.context_data['payment_methods']), [self.card1, self.card2])
        self.assertEqual(response.context_data['profile'], self.profile)

    def test_context_data_is_correct_on_manage_addresses_view(self):
        self.client.login(email='mo@abv.bg', password='password')
        response = self.client.get(reverse('manage addresses', kwargs={'username': 'mo'}))
        self.assertQuerysetEqual(list(response.context_data['addresses']), [self.address1])
        self.assertEqual(response.context_data['profile'], self.profile)

