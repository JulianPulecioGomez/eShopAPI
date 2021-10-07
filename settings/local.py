from .base import *

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'eshopdb',
        'USER': 'postgres',
        'PASSWORD': 's3cret',
        # 'HOST': 'Servers.postgres.database.azure.com',
        # 'PORT': '5432'
    }
}