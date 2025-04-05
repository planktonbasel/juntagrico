"""
Django settings for demo project.
"""

import os
import ast

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('JUNTAGRICO_SECRET_KEY')

DEBUG = False

ALLOWED_HOSTS = ['my.planktonbasel.ch']
CSRF_TRUSTED_ORIGINS = ['https://my.planktonbasel.ch']

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'djrichtextfield',
    'juntagrico_planktonbasel',
    'juntagrico_billing',
    'juntagrico',
    'fontawesomefree',
    'import_export',
    'impersonate',
    'crispy_forms',
    'adminsortable2',
    'polymorphic',
]

ROOT_URLCONF = 'juntagrico_planktonbasel.urls'

DATABASES = {
    'default': {
        'ENGINE': os.environ.get('JUNTAGRICO_DATABASE_ENGINE','django.db.backends.postgresql'), 
        'NAME': os.environ.get('JUNTAGRICO_DATABASE_NAME','postgres_production'), 
        'USER': os.environ.get('JUNTAGRICO_DATABASE_USER', 'postgres'),
        'PASSWORD': os.environ.get('JUNTAGRICO_DATABASE_PASSWORD'),
        'HOST': os.environ.get('JUNTAGRICO_DATABASE_HOST', 'localhost'),
        'PORT': os.environ.get('JUNTAGRICO_DATABASE_PORT', ''),
    }
}

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.template.context_processors.request',
                'django.contrib.messages.context_processors.messages',
            ],
            'loaders': [
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader'
            ],
            'debug' : False
        },
    },
]

WSGI_APPLICATION = 'juntagrico_planktonbasel.wsgi.application'


LANGUAGE_CODE = 'de'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

USE_TZ = True
TIME_ZONE='Europe/Zurich'

DATE_INPUT_FORMATS =['%d.%m.%Y',]

AUTHENTICATION_BACKENDS = (
    'juntagrico.util.auth.AuthenticateWithEmail',
    'django.contrib.auth.backends.ModelBackend'
)


MIDDLEWARE = [
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'impersonate.middleware.ImpersonateMiddleware',
    'django.contrib.sites.middleware.CurrentSiteMiddleware'
]

DJRICHTEXTFIELD_CONFIG = {
    'js': ['/static/juntagrico/external/tinymce/tinymce.min.js'],
    'init_template': 'djrichtextfield/init/tinymce.js',
    'settings': {
        'menubar': False,
        'plugins': 'link  lists',
        'toolbar': 'undo redo | bold italic | alignleft aligncenter alignright alignjustify | outdent indent | bullist numlist | link'
    }
}

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'INFO',
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': os.getenv('DJANGO_LOG_LEVEL', 'INFO'),
            'propagate': False,
        },
    },
}

EMAIL_HOST = os.environ.get('JUNTAGRICO_EMAIL_HOST')
EMAIL_HOST_USER = os.environ.get('JUNTAGRICO_EMAIL_USER')
EMAIL_HOST_PASSWORD = os.environ.get('JUNTAGRICO_EMAIL_PASSWORD')
EMAIL_PORT = int(os.environ.get('JUNTAGRICO_EMAIL_PORT', '25' ))
EMAIL_USE_TLS = os.environ.get('JUNTAGRICO_EMAIL_TLS', 'False')=='True'
EMAIL_USE_SSL = os.environ.get('JUNTAGRICO_EMAIL_SSL', 'False')=='True'
FROM_FILTER = ast.literal_eval(os.environ.get('JUNTAGRICO_FROM_FILTER'))
DEFAULT_FROM_EMAIL = os.environ.get('JUNTAGRICO_DEFAULT_FROM')

SESSION_SERIALIZER = 'django.contrib.sessions.serializers.PickleSerializer'
STORAGES = {
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },
    "staticfiles": {
        "BACKEND": "django.contrib.staticfiles.storage.ManifestStaticFilesStorage",
    },
}

WHITELIST_EMAILS = []

def whitelist_email_from_env(var_env_name):
    email = os.environ.get(var_env_name)
    if email:
        WHITELIST_EMAILS.append(email.replace('@gmail.com', '(\+\S+)?@gmail.com'))


if DEBUG is True:
    for key in os.environ.keys():
        if key.startswith("JUNTAGRICO_EMAIL_WHITELISTED"):
            whitelist_email_from_env(key)
            


STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'

IMPERSONATE = {
    'REDIRECT_URL': '/my/profile',
}

LOGIN_REDIRECT_URL = "/"

"""
    File & Storage Settings
"""
ADMIN_MEDIA_PREFIX = STATIC_URL + 'admin/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

"""
     Crispy Settings
"""
CRISPY_TEMPLATE_PACK = 'bootstrap4'

"""
     juntagrico Settings
"""
ORGANISATION_NAME = os.environ.get('ORGANISATION_NAME')
ORGANISATION_LONG_NAME = os.environ.get('ORGANISATION_LONG_NAME')
ORGANISATION_ADDRESS = ast.literal_eval(os.environ.get('ORGANISATION_ADDRESS'))
ORGANISATION_BANK_CONNECTION = ast.literal_eval(os.environ.get('ORGANISATION_BANK_CONNECTION'))
SHARE_PRICE = os.environ.get('SHARE_PRICE')
ENABLE_SHARES = os.environ.get('ENABLE_SHARES')
BUSINESS_YEAR_START = ast.literal_eval(os.environ.get('BUSINESS_YEAR_START'))
BUSINESS_YEAR_CANCELATION_MONTH = int(os.environ.get('BUSINESS_YEAR_CANCELATION_MONTH'))

ENABLE_REGISTRATION = False

CONTACTS = {
    "general": os.environ.get('INFO_EMAIL')
}

ORGANISATION_WEBSITE = {
    'name': os.environ.get('SERVER_URL'),
    'url': 'https://' + os.environ.get('SERVER_URL')
}

IMPORT_EXPORT_EXPORT_PERMISSION_CODE = 'view'

#STYLES = {'static': ['/juntagrico-planktonbasel/css/customize.css']}
