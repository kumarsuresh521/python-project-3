"""
Django settings for example project.

Generated by 'django-admin startproject' using Django 2.0.7.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('HUB_EXAMPLE_STORE_SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('HUB_EXAMPLE_STORE_DEBUG')

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.postgres'
]

THIRD_PARTY_APP = [
    'rest_framework',
    'django_filters',
    'pgcrypto',
]

LOCAL_APPS = [
    'store',
]

INSTALLED_APPS += THIRD_PARTY_APP + LOCAL_APPS

MIDDLEWARE = [
    'django.middleware.common.CommonMiddleware',
]
APP_VERSION = [
    'v1',
]

ROOT_URLCONF = 'example.urls'

WSGI_APPLICATION = 'example.wsgi.application'

### REST FRAMEWORK SETTING ###
'''
Namespaces are one honking great idea - let's do more of those!

Configuration for REST framework is all namespaced inside a
single Django setting, named REST_FRAMEWORK.

If you need to access the values of REST framework's API
settings in your project, you should use the api_settings
object.

from rest_framework.settings import api_settings
'''
REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': (
        'example.core.renderers.ApiRenderer',
    ),
    'EXCEPTION_HANDLER': 'example.core.exceptions.api_exception_handler',
}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('HUB_EXAMPLE_STORE_DATABASE_NAME'),
        'USER': os.environ.get('HUB_EXAMPLE_STORE_DATABASE_USERNAME'),
        'PASSWORD': os.environ.get('HUB_EXAMPLE_STORE_DATABASE_PASSWORD'),
        'HOST': os.environ.get('HUB_EXAMPLE_STORE_DATABASE_HOST'),
        'PORT': os.environ.get('HUB_EXAMPLE_STORE_DATABASE_PORT'),
    }
}

STATIC_URL = '/static/'

MEDIA_URL = '/media/'

STATIC_ROOT = os.path.join(BASE_DIR, 'public', 'static')

MEDIA_ROOT = os.path.join(BASE_DIR, 'public', 'media')

AWS_STORE_IMAGE_PATH = r'develop/store'

TIME_ZONE = 'UTC'

KEY_PATH = os.path.abspath(os.path.join(BASE_DIR, 'keys'))

PUBLIC_PGP_KEY_PATH = os.path.abspath(os.path.join(KEY_PATH, 'public.key'))
PRIVATE_PGP_KEY_PATH = os.path.abspath(os.path.join(KEY_PATH, 'private.key'))

# Used by PGPPublicKeyField used by default if not specified by the db
PUBLIC_PGP_KEY = open(PUBLIC_PGP_KEY_PATH).read()
PRIVATE_PGP_KEY = open(PRIVATE_PGP_KEY_PATH).read()

# Used by TextHMACField and PGPSymmetricKeyField if not specified by the db
PGCRYPTO_KEY='asdljkOPIERUY)(*&^%$#'

BANK_ACCOUNT_VERIFY_URL = "http://api.addressy.com/BankAccountValidation/Interactive/Validate/v2/json.ws"
BANK_ACCOUNT_VERIFY_KEY = 'HE73-TM42-CN59-TN99'

HUB_EXAMPLE_USER_KAFKA_SERVER = os.environ.get('HUB_EXAMPLE_USER_KAFKA_SERVER')
ENABLE_KAFKA = os.environ.get('HUB_EXAMPLE_STORE_ENABLE_KAFKA')
