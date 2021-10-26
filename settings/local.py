from .base import *

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'eShop',
        'USER': 'admin',
        'PASSWORD': 's3cret97021',
        'HOST': 'db-eshop.cn3ampooiuvx.us-east-1.rds.amazonaws.com',
        'PORT': '3306'
    }
}