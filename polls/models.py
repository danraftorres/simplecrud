from django.db import models

# Create your models here.
class Article(models.Model):
    image = models.ImageField(upload_to='uploads/')
