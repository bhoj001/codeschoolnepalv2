from .settings import *
DEBUG = False
import os
# Allowed host configuration
ALLOWED_HOSTS = [
    '127.0.0.1'
    'codeschoolnepal.com',
    'www.codeschoolnepal.org'
]

CODESCHOOLNEPAL_DB_NAME = os.getenv('CODESCHOOLNEPAL_DB_NAME')
CODESCHOOLNEPAL_DB_HOST = os.getenv('CODESCHOOLNEPAL_DB_HOST')
CODESCHOOLNEPAL_DB_PORT = os.getenv('CODESCHOOLNEPAL_DB_PORT')
CODESCHOOLNEPAL_DB_USERNAME = os.getenv('CODESCHOOLNEPAL_DB_USERNAME')
CODESCHOOLNEPAL_DB_PASSWORD = os.getenv('CODESCHOOLNEPAL_DB_PASSWORD')


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': CODESCHOOLNEPAL_DB_NAME,
        'USER': CODESCHOOLNEPAL_DB_USERNAME,
        'PASSWORD':CODESCHOOLNEPAL_DB_PASSWORD,
        'HOST': CODESCHOOLNEPAL_DB_HOST,
        'PORT': CODESCHOOLNEPAL_DB_PORT,
    }
}