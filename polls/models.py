from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(null=True, blank=True)


class Article(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(null=True, blank=True)
    quantity = models.IntegerField(default=0)
    image = models.ImageField(upload_to='uploads/')
    category = models.ForeignKey(Category,default=None, on_delete=models.CASCADE, related_name='articles')
