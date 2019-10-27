"""
Django settings for core project.

Generated by 'django-admin startproject' using Django 2.2.1.
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '983_d$jg#*b9p)4k&p%k-qwqc&jgp_wi*cl^(io$z+gxodf16xtdkujie&%wki+(h4hx4ewb4s%w((&*^))=hww^*og5&xeryu1o1uwag!5a!ckhfdht4'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False


ALLOWED_HOSTS = ['clicpust.cseai.com', 'www.clicpust.cseai.com']
# ALLOWED_HOSTS = []

AUTH_USER_MODEL = 'account.User'

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # postgres
    'django.contrib.postgres',

    # third party
    'crispy_forms',
    'rest_framework',
    'notifications',

    # local apps
    'account',
    'academic',
    'member',
    'resource',
    'transaction',
    'service',
    'amtd',
    'post',
    'comment',
    'messenger',
]

# added by belal from trdjango19
CRISPY_TEMPLATE_PACK = 'bootstrap4'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# added by belal from trdjango19
LOGIN_URL = "/login/"

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates'),
                 os.path.join(BASE_DIR, 'templates/account'),
                 os.path.join(BASE_DIR, 'templates/academic'),
                 os.path.join(BASE_DIR, 'templates/member'),
                 os.path.join(BASE_DIR, 'templates/resource'),
                 os.path.join(BASE_DIR, 'templates/transaction'),
                 os.path.join(BASE_DIR, 'templates/service'),
                 os.path.join(BASE_DIR, 'templates/amtd'),
                 os.path.join(BASE_DIR, 'templates/post'),
                 os.path.join(BASE_DIR, 'templates/comment'),
                 os.path.join(BASE_DIR, 'templates/messenger'),
                 os.path.join(BASE_DIR, 'templates/base_segments'),
                 os.path.join(BASE_DIR, 'templates/core'),
                 ],
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

WSGI_APPLICATION = 'core.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'clicpustv00',
        'USER': 'dbuser',
        'PASSWORD': 'dbpassword',
        'HOST': 'localhost',
        'PORT': '',
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'


STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
    # '/var/www/static/',
]

STATIC_ROOT = os.path.join(
    os.path.dirname(os.path.dirname(BASE_DIR)),
    'public', 'clicpust', 'static_cdn'
)

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(
    os.path.dirname(os.path.dirname(BASE_DIR)),
    'public', 'clicpust', 'media_cdn'
)
