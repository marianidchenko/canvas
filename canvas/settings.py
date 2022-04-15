import os
from pathlib import Path

import cloudinary

from canvas import middlewares

BASE_DIR = Path(__file__).resolve().parent.parent

APP_ENVIRONMENT = os.getenv('APP_ENVIRONMENT')

SECRET_KEY = os.getenv('SECRET_KEY')

DEBUG = os.getenv('DEBUG', 'False') == 'True'

ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', 'localhost 127.0.0.1').split(' ')

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
    'crispy_forms',
]

CRISPY_TEMPLATE_PACK = 'bootstrap3'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'canvas.middlewares.handle_exception'
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

AUTH_PASSWORD_VALIDATORS = []

if APP_ENVIRONMENT == 'Production':
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': os.getenv("DB_NAME"),
            'USER': os.getenv("DB_USER"),
            'PASSWORD': os.getenv("DB_PASSWORD"),
            'HOST': os.getenv("DB_HOST"),
            'PORT': '5432',
            'TEST': {
                'NAME': 'canvas_testing_db',
            }
        },
    }
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

else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': os.getenv("DB_NAME", "canvas_db"),
            'USER': os.getenv("DB_USER", "postgres"),
            'PASSWORD': os.getenv('DB_PASSWORD', "1123QwER"),
            'HOST': os.getenv("DB_HOST", "127.0.0.1"),
            'PORT': '5432',
            'TEST': {
                'NAME': 'canvas_testing_db',
            }
        },
    }

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

LOGGING = {
    'version': 1,
    'handlers': {
        'console': {
            # DEBUG, WARNING, INFO, ERROR, CRITICAL,
            'level': os.getenv("LOGGING_LEVEL"),
            'filters': [],
            'class': 'logging.StreamHandler',
        }
    },
    'loggers': {
        'django.db.backends': {
            'level': os.getenv("LOGGING_LEVEL"),
            'handlers': ['console'],
        }
    }
}

AUTH_USER_MODEL = 'auth_app.CanvasUser'

LOGOUT_REDIRECT_URL = 'logged out'

cloudinary.config(
    cloud_name="hjz5y3fhi",
    api_key="368366934282259",
    api_secret="d7M_Ji3dejYAHV_U3ZPVK8885A0",
    secure=True,
)
