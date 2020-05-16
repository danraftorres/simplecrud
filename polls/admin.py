from django.contrib import admin
from polls.models import Article, Category

# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    #model = Article
    list_display = ('name', 'description', 'get_category_name')

    def get_category_name(self, object):
        return object.category.name

    get_category_name.admin_order_field = 'category' #'category__name'
    get_category_name.short_description = 'Category name'

    

#admin.site.register([Article, Category])
