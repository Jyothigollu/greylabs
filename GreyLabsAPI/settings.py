"""
Django settings for GreyLabsAPI project.

Generated by 'django-admin startproject' using Django 5.1.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

import os
from pathlib import Path
import dj_database_url # type: ignore
from dotenv import load_dotenv
import django_heroku


# Load environment variables from a .env file if present
load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET_KEY', 'default-secret-key-for-development')
#SECRET_KEY = 'django-insecure-5&+$z^=-_f2u#jj*&n9pw&@@_!svf1-7)ekk87iw5x5_9#rz4i'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
#DEBUG = os.getenv('DEBUG', 'False').lower() in ['true', '1']

#ALLOWED_HOSTS = []
ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', '*').split(',')
ALLOWED_HOSTS = ['greylabs-a2f47a4c50d2.herokuapp.com', 'localhost', '127.0.0.1']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'api',
    'oauth2_provider',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # Ensure this is before other middleware
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


ROOT_URLCONF = 'GreyLabsAPI.urls'

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

WSGI_APPLICATION = 'GreyLabsAPI.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

"""DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'Grey_labs',
        'USER': 'root',
        'PASSWORD': 'Jyothi@2709',
        'HOST': '127.0.0.1',
        'PORT': '3307',
    }
}"""


DATABASES = {}

# Check if DATABASE_URL environment variable is set (for production)
if os.getenv('postgres://u56euen7aa0at7:p70a00046fad8d0a9f9fbf7f005ddfb77f39299a7d962631c576ec93d3a3ff7ff@c8lj070d5ubs83.cluster-czrs8kj4isg7.us-east-1.rds.amazonaws.com:5432/de2ovnl3i6appm'):
    DATABASES['default'] = dj_database_url.config(conn_max_age=600, ssl_require=True)
else:
    # Fallback to local MySQL settings (for development)
    DATABASES['default'] = {
        'ENGINE': os.getenv('DB_ENGINE', 'django.db.backends.mysql'),
        'NAME': os.getenv('DB_NAME', 'Grey_labs'),
        'USER': os.getenv('DB_USER', 'root'),
        'PASSWORD': os.getenv('DB_PASSWORD', 'Jyothi@2709'),
        'HOST': os.getenv('DB_HOST', '127.0.0.1'),
        'PORT': os.getenv('DB_PORT', '3307'),
    }
# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')


# Add this line if not already present

#DATABASES['default'] = dj_database_url.config(conn_max_age=600, ssl_require=True)


# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

django_heroku.settings(locals())

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


AUTHENTICATION_BACKENDS = [
    'oauth2_provider.backends.OAuth2Backend',
    'django.contrib.auth.backends.ModelBackend',
]

OAUTH2_PROVIDER = {
    'ACCESS_TOKEN_EXPIRE_SECONDS': 36000,
    'AUTHORIZATION_CODE_EXPIRE_SECONDS': 600,
    'REFRESH_TOKEN_EXPIRE_SECONDS': 86400,
}
AUTH0_DOMAIN = os.getenv('AUTH0_DOMAIN', 'dev-gpf8q50v3vp0hh3l.us.auth0.com')
AUTH0_CLIENT_ID = os.getenv('AUTH0_CLIENT_ID', 'YapcJdR21g5Z52qdqFmdSNO2M6xmyPUj')
AUTH0_CLIENT_SECRET = os.getenv('AUTH0_CLIENT_SECRET', 'cud73_tjY3UM0hhl0yP5jR7uLXEJ4bmzisSFLcuc07mmTghSVWujserhdC5uKbHm')
