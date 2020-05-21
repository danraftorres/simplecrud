#https://medium.com/@a01208219/forms-de-django-857edcff9307
#https://stackoverflow.com/questions/291945/how-do-i-filter-foreignkey-choices-in-a-django-modelform
#https://samulinatri.com/blog/django-modelform-tutorial/

from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'{self.id} - {self.name}'


class Article(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    image = models.ImageField(upload_to='uploads/')
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name='articles')

    def __str__(self):
        return self.name
