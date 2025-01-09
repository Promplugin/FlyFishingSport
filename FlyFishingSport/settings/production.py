from .base import *

DEBUG = False
ALLOWED_HOSTS = [ 'stage.flyfishingsport.ru', '0.0.0.0:8000', '127.0.0.1', '92.118.113.162', '188.225.27.35', 'flyfishingsport.ru', 'http://flyfishingsport.ru', 'https://flyfishingsport.ru', 'backend-46824bc8-298f-4fa1-8bf5-0b79181cf83a-http']
# CSRF_TRUSTED_ORIGINS = ['https://127.0.0.1', 'https://stage.flyfishingsport.ru', 'https://promplugin-flyfishingsport-cad9.twc1.net', 'http://flyfishingsport.ru', 'https://flyfishingsport.ru', 'https://0.0.0.0:8000']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'FlyFishingSport_DB',
        'USER': 'dbadmin',
        'PASSWORD': 'F7$mK2@bL9#q',
        'HOST': '92.118.113.162',
    }
}