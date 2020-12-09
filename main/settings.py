"""
Django settings for main project.

Generated by 'django-admin startproject' using Django 3.0.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""
from pathlib import Path
import os
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'cccoevp@#xmtvi02ty^5(+!0p7hz&rwc=4t(a5x)dc_1f$sx*t'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
    # DJANGO PRE-INSTALLED APPS
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'django_heroku',
    'gunicorn',
    # USER APPS
    'user.apps.UserConfig',
    'blog.apps.BlogConfig',
    'teams.apps.TeamsConfig',
    'meeting.apps.MeetingConfig',
    'contacts.apps.ContactsConfig',
    'attendance_request.apps.AttendanceRequestConfig',
    'hitcount',
    'todo',
    # CRISPY FORMS
    'pytz',
    # CLEANUP APP (CLEANS DELETED IMAGES FROM MEDIA)
    'django_cleanup.apps.CleanupConfig',

    # DJANGO APP
    'django.contrib.sites',

    # COMMENTS APP FOR WHOLE SITE
    'comment',
    # FORM RENDERER FOR MAIN SITE
    'bootstrap4',

    # T&C APP
    # QR CODE APP
    'qrcode',
    'taggit',
    'tinymce',

    # PINAX APPS
    "account",
    "bootstrapform",
    "pinax.templates",
    'calendarapp',

    #AutoChromeDriverInstaller
    #'chromedriver-autoinstaller',
    'admin_honeypot'
]
USE_TZ = True

MIDDLEWARE = [
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'user.onlinenowMiddelware.OnlineNowMiddleware',
    "account.middleware.LocaleMiddleware",
    "account.middleware.TimezoneMiddleware",
]

ROOT_URLCONF = 'main.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                "account.context_processors.account",
            ],
        },
    },
]
WSGI_APPLICATION = 'main.wsgi.application'



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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Calcutta'

USE_I18N = True

USE_L10N = True

USE_TZ = True


#   DJANGO SETTINGS MANUAL
#STATIC SETTINGS
STATIC_URL = '/static/'
STATIC_ROOT = 'static/'


# MEDIA
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

# CRISPY FORMS SETTINGS
CRISPY_TEMPLATE_PACK = 'bootstrap4'

# REDIRECT SETTINGS
LOGIN_URL = '/account/login'
LOGIN_REDIRECT_URL = 'home'
LOGOUT_REDIRECT_URL = '/'

# DJANGO MAIL SETTINGS
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'ynv048@gmail.com'
EMAIL_HOST_PASSWORD = '08ar1a0424'
DEFAULT_FROM_EMAIL = "GitCRTeam <Team@GITCRs>"



# TAGGIT APP
TAGGIT_CASE_INSENSITIVE = True

# Reidrect site id for postman and comments app change it if you add new site
SITE_ID = 1



# PROFILE_APP_NAME = 'accounts'
# PROFILE_MODEL_NAME = 'Account'


# DJANGO FILTER SETTINGS

FILTERS_EMPTY_CHOICE_LABEL = ''


def FILTERS_VERBOSE_LOOKUPS():
    from django_filters.conf import DEFAULTS

    verbose_lookups = DEFAULTS['VERBOSE_LOOKUPS'].copy()
    verbose_lookups.update({
        'exact': '',
        'iexact': '',
        'contains': '',
        'icontains': '',
    })
    return verbose_lookups
# DJANGO FILTER SETTINGS  ENDS HERE


INTERNAL_IPS = [
    # ...
    '127.0.0.1',
    # ...
]


# TINY MCE SETTINGS STARTS HERE
TINYMCE_INCLUDE_JQUERY = True
TINYMCE_SPELLCHECKER = True
# TINY MCE SETTINGS ENDS HERE

# ACCOUNT SETTINGS STARTS HERE
ACCOUNT_OPEN_SIGNUP = True
ACCOUNT_EMAIL_CONFIRMATION_REQUIRED = False
ACCOUNT_EMAIL_CONFIRMATION_EMAIL = False
ACCOUNT_EMAIL_CONFIRMATION_AUTHENTICATED_REDIRECT_URL = 'account_login'