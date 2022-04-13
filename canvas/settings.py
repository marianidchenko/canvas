import os
from pathlib import Path

import cloudinary

BASE_DIR = Path(__file__).resolve().parent.parent

APP_ENVIRONMENT = os.getenv('APP_ENVIRONMENT')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-#q1e)dw5%o9vaz2%6jyd6lhjmplqwd3towk1=c67*rw(%ky+=y'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv('DEBUG', 'False') == 'True'

ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS').split(' ')

CLOUDINARY_URL = "cloudinary://368366934282259:d7M_Ji3dejYAHV_U3ZPVK8885A0@hjz5y3fhi"

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'canvas.auth_app',
    'canvas.main',
    'canvas.profile_app',

    'cloudinary',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'canvas.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'canvas.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = None

if APP_ENVIRONMENT == 'Production':
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'da233bf1qnosm3',
            'USER': 'jolitxisgllonr',
            'PASSWORD': '8aa7ee1bb90fb6a90b0ff49070983e3a5330f219da831a5e2f2ec465fa4f81c2',
            'HOST': 'ec2-52-48-159-67.eu-west-1.compute.amazonaws.com',
            'PORT': '5432',
            'TEST': {
                'NAME': 'canvas_testing_db',
            }
        },
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'canvas_db',
            'USER': 'postgres',
            'PASSWORD': '1123QwER',
            'HOST': '127.0.0.1',
            'PORT': '5432',
            'TEST': {
                'NAME': 'canvas_testing_db',
            }
        },
    }

# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

STATIC_ROOT = BASE_DIR / 'staticfiles'
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    BASE_DIR / 'static',
)

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'mediafiles'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'auth_app.CanvasUser'

LOGOUT_REDIRECT_URL = 'logged out'

cloudinary.config(
    cloud_name="hjz5y3fhi",
    api_key="368366934282259",
    api_secret="d7M_Ji3dejYAHV_U3ZPVK8885A0",
    secure=True,
)
