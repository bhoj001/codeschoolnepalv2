from .settings import *
DEBUG = False

# Allowed host configuration
ALLOWED_HOSTS = [
    '127.0.0.1'
    'codeschoolnepal.org',
    'www.codeschoolnepal.org'
]

# Database settings
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'codeschoolnepal',
        'HOST': '127.0.0.1',
		'PORT': 5432,
        'USERNAME': 'codeschoolnepal_user',
        'PASSWORD': 'codeschoolnepal@#321',
    }
}
