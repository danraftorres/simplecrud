from django.urls import path
from polls import views

app_name='polls'

urlpatterns = [
    # article
    path('article/new/', views.article_new, name='article-new'),
    path('article/list/', views.article_list, name='article-list'),

]