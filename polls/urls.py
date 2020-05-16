from django.urls import path
from polls import views

urlpatterns = [
    # author
    path('author/create/', views.create_author_view, name='create_author_view'),
    path('author/list/', views.author_list_view, name='author_list_view'),

    #book
    path('book/create/', views.create_book_view, name='create_book_view')

]