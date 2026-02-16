from django.urls import path
from . import views, api

app_name = 'books'

urlpatterns = [
    # Web views
    path('books/', views.book_list, name='book_list'),
    path('books/create/', views.create_book, name='create_book'),
    path('books/<int:pk>/', views.book_detail, name='book_detail'),
    path('books/<int:pk>/update/', views.update_book, name='update_book'),
    path('books/<int:pk>/delete/', views.delete_book, name='delete_book'),

    path('authors/', views.author_list, name='author_list'),
    path('authors/<int:pk>/', views.author_detail, name='author_detail'),

    # API endpoints (JSON)
    path('api/books/', api.BookListCreateAPI.as_view(), name='api_book_list'),
    path('api/books/<int:pk>/', api.BookRetrieveUpdateDestroyAPI.as_view(), name='api_book_detail'),
    path('api/authors/', api.AuthorListAPI.as_view(), name='api_author_list'),
    path('api/authors/<int:pk>/', api.AuthorRetrieveAPI.as_view(), name='api_author_detail'),
]
