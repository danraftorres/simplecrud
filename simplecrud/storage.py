#from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage

class MediaStorage(S3Boto3Storage):
    bucket_name = 'simplecrud'
    location = 'media'#settings.MEDIA_ROOT

# class StaticFilesStorage(S3BotoStorage):
#     location = settings.STATICFILES_LOCATION

class StaticStorage(S3Boto3Storage):
    bucket_name = 'simplecrud'
    location = 'static'