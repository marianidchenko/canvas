from django.core.exceptions import ValidationError
from django.test import TestCase

from canvas.auth_app.models import CanvasUser
from canvas.profile_app.models import Profile, PaymentMethod


class ProfileTest(TestCase):
    def setUp(self):
        CanvasUser.objects.create(email='mo@abv.bg')

    VALID_PROFILE_DATA = {
        'username': 'mo',
        'description': 'description',
        'profile_photo': '../../../static/images/logo.png'
    }

    def test_profile_create__when_data_is_valid(self):
        profile = Profile(**self.VALID_PROFILE_DATA)
        profile.user = CanvasUser.objects.get(email='mo@abv.bg')
        profile.save()
        self.assertIsNotNone(profile.pk)
        self.assertEqual(str(profile), 'mo')

    def test_profile_create__with_no_user__expect_to_fail(self):
        profile = Profile(**self.VALID_PROFILE_DATA)
        with self.assertRaises(ValidationError) as context:
            profile.full_clean()
            profile.save()
        self.assertIsNotNone(context.exception)

    def test_profile_create__with_long_username__expect_to_fail(self):
        user = CanvasUser(email='mo@abv.com')
        user.save()
        profile = Profile(username='usernameusernameusernameusername', profile_photo='../../../static/images/logo.png')
        profile.user = user
        with self.assertRaises(ValidationError) as context:
            profile.full_clean()
            profile.save()
        print(context.exception)
        self.assertIsNotNone(context.exception)


class PaymentMethodTests(TestCase):
    def setUp(self):
        CanvasUser.objects.create(email='mo@abv.bg')

    def test_create_payment_method__str_is_correct(self):
        profile = Profile(username='username', profile_photo='../../../static/images/logo.png')
        profile.user = CanvasUser.objects.get(email='mo@abv.bg')
        profile.save()
        card = PaymentMethod.objects.create(card_number='4532297793563207', card_expiry='12/23', card_cvv='123', profile=profile)
        card.save()
        self.assertEqual(str(card), '**** **** **** 3207')
