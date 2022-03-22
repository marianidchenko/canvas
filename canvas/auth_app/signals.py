from django.contrib import messages
from django.contrib.auth.signals import user_logged_out
from django.dispatch import receiver


@receiver(user_logged_out)
def extra_logout(sender, request, user, **kwargs):
    messages.add_message(request, messages.SUCCESS, 'Successfully logged out.')
