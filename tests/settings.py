"""
Django settings for tests project.

Generated by 'django-admin startproject' using Django 3.0.8.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
import datetime

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ktwi1_u23!jmbek$w&4)7odm5ie5j$+$_i$s&qv1by@5%h*n-5'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    # qx_base
    'qx_base.qx_core',
    'qx_base.qx_rest',
    'qx_base.qx_user',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'tests.urls'

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

WSGI_APPLICATION = 'tests.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',  # noqa
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',  # noqa
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',  # noqa
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',  # noqa
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'

# qx_base
JWT_AUTH = {
    'JWT_REFRESH_EXPIRATION_DELTA': datetime.timedelta(days=7),
}
# qx_base
JWT_TOKEN_KEYWORD = "Token"
# RestFramework
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'qx_base.qx_user.auth.JwtAuthentication',  # qx_base
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ),
    'DEFAULT_PARSER_CLASSES': [
        'rest_framework.parsers.JSONParser',
    ],
    'DEFAULT_PAGINATION_CLASS':
        'qx_base.qx_rest.paginations.Pagination',  # qx_base
    'DEFAULT_FILTER_BACKENDS': (
        'django_filters.rest_framework.DjangoFilterBackend',
        'rest_framework.filters.OrderingFilter',
        'rest_framework.filters.SearchFilter',
    ),
    'EXCEPTION_HANDLER': 'qx_base.qx_rest.handlers.rest_exception_handler',  # noqa qx_base
    'PAGE_SIZE': 15,
}
# qx_base
REDIS_HOST = "127.0.0.1"
REDIS_PORT = 6379
REDIS_PASSWORD = ""
REDIS_URL = "redis://:{}@{}:{}".format(
    REDIS_PASSWORD,
    REDIS_HOST,
    REDIS_PORT)
# qx_base
IGNORE_CHECK_SIGN_PATH = []
# qx_base
SIGNATURE_PUBLIC_KEY = """-----BEGIN PUBLIC KEY-----
MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDLSICXShm0e2IJv2e0e1iyVQ9N
EdfGTjOahpd9tEIhExud7e1AND1Z5Drrd2ONgZcMmaoencs3GbfCbNz3KKr5dEHz
TEb7NZVquo+HeZF9MhrzpeZ4mZlRtqQQuxf9+vIjWKlohhq1TjnXCO2mdn0yOk//
jQhZY9nOs9I9S1J74QIDAQAB
-----END PUBLIC KEY-----"""
SIGNATURE_PRIVATE_KEY = """-----BEGIN RSA PRIVATE KEY-----
MIICXQIBAAKBgQDLSICXShm0e2IJv2e0e1iyVQ9NEdfGTjOahpd9tEIhExud7e1A
ND1Z5Drrd2ONgZcMmaoencs3GbfCbNz3KKr5dEHzTEb7NZVquo+HeZF9MhrzpeZ4
mZlRtqQQuxf9+vIjWKlohhq1TjnXCO2mdn0yOk//jQhZY9nOs9I9S1J74QIDAQAB
AoGAS9LeTBASqHRBLDudtf8wJUx+6ZNXNZujueasCPI8nFOhQHYnwYP6wlXT+FJO
6tBEhCmo/8SBsSrBlR7ACNy9cKY/1bZKFFmPUDdKnTTeqgKqbvBhe0WHWsfQoTOW
tihu0X56IeSpCsSihUd+5aKpSotfSaTuYZbeDjsvy/i+FrUCQQDrCrEYLCxR47KR
Gk+++wr1W0TjulNPYqVY8Wfi7FoMQunbn2mLCxc6OgyYRmS9BCUuZ77nDR3WHWtO
3foUksj/AkEA3WjbUgw5SIGEURkYsZ02dPXfF0nWvFNiuMB7qe9yeCLaIiGbi+15
AkbWSMWy6nFnZW2Gd1YuRZ2Wb0pK2mbbHwJAcQzpdTj58EFWyBghtzhEYxMNJYOf
QpWt9gPW9fy8qx0cInigaTJib60wFaX2Gjv+Lj3UQom6ihwIWxzFhlO7vQJBALZ8
tkfpy0z3cxdkl/XMnhXIkRegxFx0XenovARUVwSttRxslse98v7tY7CXQd/5mD8B
BtNVNM4sFNGlagyYugECQQCAEKAVJw/1pwrS5B+F9wlA9Ez7fI0uzFOcrc4RauXA
ElBD6PTOifsl8TBQ2cQhPC//+/oP9wJlbXO0+G4VPSuM
-----END RSA PRIVATE KEY-----"""
