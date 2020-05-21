from django.urls import path
from polls import views

app_name = 'polls'

urlpatterns = [
    # article
    path('article/create/', views.article_create_view, name='article-create'),
    path('article/', views.article_list_view, name='article-list'),
    path('article/<int:id>/edit', views.article_edit_view, name='article-edit'),
    path('article/<int:id>/delete', views.article_delete_view, name='article-delete'),
    path('article/<int:id>/update', views.article_udpate_view, name='article-update'),
]
