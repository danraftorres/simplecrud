from .base import *

ALLOWED_HOSTS = ['damp-plains-78859.herokuapp.com']

MIDDLEWARE += []

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases
DATABASES = {
    'default': env.db('DATABASE_URL', default='')
}