from .base import *


DEBUG = 'True'

ALLOWED_HOSTS = ['localhost', '127.0.0.1']

INSTALLED_APPS += [
    'debug_toolbar',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',  # Или любая другая БД для разработки
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

MIDDLEWARE += [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

INTERNAL_IPS = [
    '127.0.0.1',
]