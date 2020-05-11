from django.urls import path
from polls import views

urlpatterns = [
    path('author/create/', views.create_author_view, name='create_author_view'),
    path('author/list/', views.author_list_view, name='author_list_view')
]