from .base import *

ALLOWED_HOSTS = ['damp-plains-78859.herokuapp.com']

MIDDLEWARE += []

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': env.str('DATABASE_ENGINE', default='django.db.backends.sqlite3'),
        'NAME': env.str('DATABASE_NAME', default=os.path.join(BASE_DIR, 'db.sqlite3')),
        'USER': env.str('DATABASE_USER', default=''),
        'PASSWORD': env.str('DATABASE_PASSWORD', default=''),
        'HOST': env.str('DATABASE_HOST', default=''),
        'PORT': env.str('DATABASE_PORT', default='')
    }
}