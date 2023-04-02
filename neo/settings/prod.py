from .base import *

DATABASES = {
    'default': {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "neo",
        "USER":"postgres",
        "PASSWORD":'2912',
        "HOST":"localhost"

    }
}

SECRET_KEY = 'ly19&2+c#onohxpodxnrlpvx3#)wc_qw!nvnb0^)oe%_yj$vf4'
ALLOWED_HOSTS = ['ecommerce.pythonanywhere.com']

MEDIA_ROOT = '/home/ecommerce/ecommerce/media'
MEDIA_URL = '/media/'
STATIC_ROOT = '/home/ecommerce/ecommerce/static'
STATIC_URL = '/static/'
