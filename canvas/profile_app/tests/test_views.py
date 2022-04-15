from django.test import TestCase
from django.urls import reverse

from canvas.auth_app.models import CanvasUser
from canvas.common_tools.helpers import get_profile_by_username
from canvas.profile_app.models import Profile


class ProfileDetailsViewTest(TestCase):
    def setUp(self):
        user = CanvasUser.objects.create(email='mo@abv.bg')
        Profile.objects.create(username='mo', profile_photo='../../../static/images/logo.png', user=user)

    def test_view_returns_correct_profile_for_queryset(self):

        self.client.post(
            reverse('profile details', kwargs={'username': 'mo'})
        )
        self.assertTemplateUsed('profile/profile_detail.html')