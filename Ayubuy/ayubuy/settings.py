# settings.py

# Add this line to specify the default primary key type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

""""
Django settings for ayubuy project.

Generated by 'django-admin startproject' using Django 3.1.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve(strict=True).parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv("DEBUG", "True").lower() in ("true", "1", "yes")  # default to "False" if not set

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'category',
    'accounts',
    'store',
    'carts',
    'orders',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django_session_timeout.middleware.SessionTimeoutMiddleware',
]

SESSION_EXPIRE_SECONDS = 3600  # 1 hour - Adjust this as per your requirement
SESSION_EXPIRE_AFTER_LAST_ACTIVITY = True  # Automatically expire session after inactivity
SESSION_EXPIRE_AT_BROWSER_CLOSE = True  # Expire session when the browser is closed

# Session cookie age (the expiration time of the session in seconds)
SESSION_COOKIE_AGE = SESSION_EXPIRE_SECONDS

# Define where users are redirected when their session expires
LOGIN_URL = 'accounts/login/'  # This is the URL where the user will be redirected
SESSION_TIMEOUT_REDIRECT = 'accounts/login/' # Explicit redirect to login page

ROOT_URLCONF = 'ayubuy.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',  
        # Specifies the Django template engine as the backend
        
        'DIRS': ['templates'],  
        # Defines the directory where Django should look for template files (custom templates)

        'APP_DIRS': True,  
        # Enables automatic discovery of templates within each installed app's `templates` directory
        
        'OPTIONS': {
            'context_processors': [  
                # List of context processors that inject additional data into templates
                
                'django.template.context_processors.debug',  
                # Enables debugging information in templates (useful in development)
                
                'django.template.context_processors.request',  
                # Makes the `request` object available in templates
                
                'django.contrib.auth.context_processors.auth',  
                # Provides authentication-related context (e.g., `user` object)
                
                'django.contrib.messages.context_processors.messages',  
                # Enables messages framework for displaying user notifications
                
                'category.context_processors.menu_links',  
                # Custom context processor: Injects category menu links into templates
                
                'carts.context_processors.counter',  
                # Custom context processor: Provides cart item count in templates
            ],
        },
    },
]


WSGI_APPLICATION = 'ayubuy.wsgi.application'

AUTH_USER_MODEL = 'accounts.Account'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR /'static'
STATICFILES_DIRS = [
    'ayubuy/static',
]


# Media files configurations
MEDIA_URL = '/media/'
STATIC_ROOT = BASE_DIR /'media'

# Django Messages 
from django.contrib.messages import constants as messages

MESSAGE_TAGS = {
    messages.ERROR: "danger",
}

# Email Configuration
EMAIL_BACKEND = os.getenv("EMAIL_BACKEND")
EMAIL_HOST = os.getenv("EMAIL_HOST")
EMAIL_PORT = int(os.getenv("EMAIL_PORT", 587)) 
EMAIL_USE_TLS = os.getenv("EMAIL_USE_TLS", "False").lower() in ("true", "1", "yes")
EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD")
DEFAULT_FROM_EMAIL = os.getenv("DEFAULT_FROM_EMAIL")

