from .common import *

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'euro2016',
        'USER': 'euro2016',
        'PASSWORD': 'franca',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}

DEBUG = False
