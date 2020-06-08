from .base import *

ALLOWED_HOSTS = env.list('DJANGO_ALLOWED_HOSTS', default=['damp-plains-78859.herokuapp.com', ])

WHITENOISE_MIDDLEWARE = ['whitenoise.middleware.WhiteNoiseMiddleware', ]
MIDDLEWARE = WHITENOISE_MIDDLEWARE + MIDDLEWARE

INSTALLED_APPS += ['storages', ]

# Simplified static file serving.
# https://warehouse.python.org/project/whitenoise/
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases
DATABASES = {
    'default': env.db('DATABASE_URL', default='')
}

# AWS settings
AWS_QUERYSTRING_AUTH = False
AWS_ACCESS_KEY_ID = env.str('AWS_ACCESS_KEY_ID', default='')
AWS_SECRET_ACCESS_KEY = env.str('AWS_SECRET_ACCESS_KEY', default='')
AWS_STORAGE_BUCKET_NAME = env.str('S3_BUCKET_NAME', default='simplecrud')
MEDIA_URL = 'http://%s.s3.amazonaws.com/your-folder/' % AWS_STORAGE_BUCKET_NAME
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'