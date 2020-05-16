from django.contrib import admin
from polls.models import Article, Category
#from admin_site import custom_admin_site

# Register your models here.
@admin.register(Category)#, Article, site=custom_admin_site)
class CategoryAdmin(admin.ModelAdmin):   
    pass
#     list_display = ('name', 'description')


# @admin.register(Category)
# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ('name', 'description')

#admin.site.register([Article, Category])