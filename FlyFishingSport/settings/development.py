from .base import *


DEBUG = 'True'

ALLOWED_HOSTS = ['*']
CSRF_TRUSTED_ORIGINS = ['http://127.0.0.1:8000']


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',  # Или любая другая БД для разработки
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


INTERNAL_IPS = [
    '127.0.0.1',
]