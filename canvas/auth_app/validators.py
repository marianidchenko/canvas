from django.forms import forms

from canvas.profile_app.models import Profile


def validate_unique_username(username):
    for profile in Profile.objects.all():
        if profile.username == username:
            raise forms.ValidationError(f"Username {username} is taken.")