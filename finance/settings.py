"""
Django settings for finance project.

Generated by 'django-admin startproject' using Django 1.8.4.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import socket

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

ADMINS = (('Yohan Estiven Arias', 'jsarias0514@gmail.com'))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'sv5&r6$xwi-^l745s!(rqrsqh8pv=x^lw-98^1d=j5j4k4-64f'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = socket.gethostname() == 'MacBook-Pro-de-Johan.local'

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = (
    'storages',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'finance.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'finance.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

if DEBUG:
    DATABASES = {
        'default':{
            'ENGINE':'django.db.backends.postgresql_psycopg2',
            'NAME':'finance',
            'USER':'postgres',
            'PASSWORD': os.environ['pass_db'],
            'HOST':'localhost',
            'PORT':'5433',

        }
    }

else:
    import dj_database_url
    DATABASES = {
        'default': dj_database_url.config()
    }


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/Bogota'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATICFILES_DIRS = (
            os.path.join(BASE_DIR, 'static'),
        )

AWS_HEADERS = {  # see http://developer.yahoo.com/performance/rules.html#expires
            'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
            'Cache-Control': 'max-age=94608000',
        }
AWS_STORAGE_BUCKET_NAME = 'personalfinance'
AWS_ACCESS_KEY_ID = os.environ['s3_key_id']
AWS_SECRET_ACCESS_KEY = os.environ['s3_access_key']
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
STATIC_URL = "https://%s/" %AWS_S3_CUSTOM_DOMAIN
STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'

