from . import *

SECRET_KEY = '-~aO;| F;rE[??/w^zcumh(9'
DEBUG = False
ALLOWED_HOSTS = ['178.62.117.192']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql', # on utilise l'adaptateur postgresql
        'NAME': 'pur_beurre', # le nom de notre base de données créée précédemment
        'USER': 'mehdi', # attention : remplacez par votre nom d'utilisateur !!
        'PASSWORD': 'azerty',
        'HOST': '',
        'PORT': '',
    }
}

