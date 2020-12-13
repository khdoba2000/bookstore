
from django.conf.urls import url
from . import views
from django.shortcuts import get_object_or_404
from django.urls import include, path
from .models import Book
from .views import inc, dec, book_list, book_create, book_detail, book_update, book_delete
app_name = 'backend'

urlpatterns = [
    path('', book_list.as_view(), name="book_list"),
    path('create', book_create.as_view(), name="book_create"),
    path('book/<int:pk>', book_detail.as_view(), name="book_detail"),
    path('book/<int:pk>/update', book_update.as_view(), name="book_update"),
    path('book/<int:pk>/delete', book_delete.as_view(), name="book_delete"),
    path('book_inc/<int:pk>', inc.as_view(), name='book_inc'),
    path('book_dec/<int:pk>', dec.as_view(), name="book_dec"),
    
    
   
]

