from django import forms
from django.contrib.auth import forms as auth_forms, get_user_model

from canvas.profile_app.models import Profile

UserModel = get_user_model()


class UserRegistrationForm(auth_forms.UserCreationForm):
    username = forms.CharField(
        max_length=25
    )

    profile_photo = forms.ImageField()

    class Meta:
        model = UserModel
        fields = ('email',)

    def clean_email(self):
        return self.cleaned_data['email']

    def save(self, commit=True):
        user = super().save(commit=commit)

        profile = Profile(
            username=self.cleaned_data['username'],
            profile_photo=self.cleaned_data['profile_photo'],
            user=user,
        )
        if commit:
            profile.save()

        return user

