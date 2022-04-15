import cloudinary
from django.forms import forms
from canvas.profile_app.models import Profile


def validate_unique_username(username):
    username_qs = Profile.objects.filter(username=username)
    if username_qs.exists():
        raise forms.ValidationError(f"Username {username} is already taken.")


def validate_photo(img):
    available_formats = [
        'png',
        'jpeg',
        'jpg',
        'jfif',
    ]
    if type(img) == cloudinary.CloudinaryResource:
        pass
    elif type(img) == cloudinary.CloudinaryImage:
        extension = img.format
        if extension not in available_formats:
            raise forms.ValidationError(
                f"{extension} files are not allowed. Allowed formats are {', '.join(available_formats)}")
        return img
    else:
        extension = img.name.split(".")[-1]
        if extension not in available_formats:
            raise forms.ValidationError(
                f"{extension} files are not allowed. Allowed formats are {', '.join(available_formats)}")
        return img
