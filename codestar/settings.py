"""
Django settings for codestar project.

Generated by 'django-admin startproject' using Django 4.2.14.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

import os
import dj_database_url
if os.path.isfile('env.py'):
    import env
from pathlib import Path

# The dj_database_url import is used to convert the database URL into a format
#  that Django can use to connect to an external database server.

# The code uses another method from the os module to check if the env.py file path exists. 
# If it does, then it will be imported. If it does not exist, the env import will not be 
# attempted so that no error will occur. For example, when the app runs on Heroku, 
# there will be no env.py file to load

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Create a TEMPLATES_DIR constant to build a path for our subdirectory 'templates'.
TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = 'django-insecure-c$edrwg21a2h7g^d5mjf4^#6cax*%5fp)0+vgmf#g43&10nrm1'
SECRET_KEY = os.environ.get('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['8000-eneliviu-djangoblogpy-h09fu1py07c.ws.codeinstitute-ide.net', 
                 '.herokuapp.com']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'crispy_forms',       # no migrations files to migrate for crispy_forms.
    'crispy_bootstrap5',  # no migrations files to migrate for crispy_bootstrap5.
    'django_summernote',
    'blog',
    'about',
]


SITE_ID = 1  # so that Django can handle multiple sites from one database. 
             # We need to give each project an ID value so that the database 
             # is aware of which project is contacting it. 
             # We only have one site here using our one database, 
             # but we'll still need to tell Django the site number of 1 explicitly.


LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'
# The redirection URLs are also added so that after we've logged in or logged out, 
# the site will automatically redirect us to the home page.


CRISPY_ALLOWED_TEMPLATE_PACKS = 'bootstrap5'
CRISPY_TEMPLATE_PACK = 'bootstrap5'
# These constants set bootstrap5 as the allowed template pack and as the default template pack for project. 
# This choice of default template pack is to match the Bootstrap5 CSS and JS files
# already used in project base.html template.


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'allauth.account.middleware.AccountMiddleware',  # middleware for the allauth.account app added to INSTALLED_APPS
]

ROOT_URLCONF = 'codestar.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATES_DIR],  # templates directory in the base, or top-level directory.
        'APP_DIRS': True,  # Django looks for a templates directory inside all app directories.
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

WSGI_APPLICATION = 'codestar.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

# This code uses os.environ.get to get the value stored in the DATABASE_URL 
# environment variable. The value is then parsed using dj_database_url to put it
# in a format that Django can use.
DATABASES = {
    'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
}

CSRF_TRUSTED_ORIGINS = [
    "https://*.codeanyapp.com",
    "https://*.herokuapp.com",
    'https://*.127.0.0.1',
    "https://*8000-eneliviu-djangoblogpy-h09fu1py07c.ws.codeinstitute-ide.net"
]
# Cross-Site Request Forgery: when an attacker's website tries to make requests to another site on your behalf.
# The list of the trusted origins for requests.
# Need to add both your local development server URL domain 
# and the production server URL domain to allow you to add blog post
# content from the admin dashboard.
# The subdomain is wildcarded with a *.

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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


ACCOUNT_EMAIL_VERIFICATION = 'none'  # not using email verification in this project

# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')  # collect all static files from all apps in 'staticfiles' directory. 
# Django will serve static files from 'staticfiles' directory.

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
