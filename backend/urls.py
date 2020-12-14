
from django.conf.urls import url
from . import views
from django.shortcuts import get_object_or_404
from django.urls import include, path
from .views import inc, dec, book_model_list, book_model_create, book_model_detail, book_model_update, book_model_delete
from .views import book_list, book_create, book_detail, book_update, book_delete
app_name = 'backend'

urlpatterns = [
    path('', book_model_list.as_view(), name="book_model_list"),
    path('create_model', book_model_create.as_view(), name="book_model_create"),
    path('book_model/<int:pk>', book_model_detail.as_view(), name="book_model_detail"),
    path('book_model/<int:pk>/update', book_model_update.as_view(), name="book_model_update"),
    path('book_model/<int:pk>/delete', book_model_delete.as_view(), name="book_model_delete"),
    path('book_model_inc/<int:pk>', inc.as_view(), name='book_model_inc'),
    path('book_model_dec/<int:pk>', dec.as_view(), name="book_model_dec"),
    
    path('book_list', book_list.as_view(), name="book_list"),
    path('create_book', book_create.as_view(), name="book_create"),
    path('book/<int:pk>', book_detail.as_view(), name="book_detail"),
    path('book/<int:pk>/update', book_update.as_view(), name="book_update"),
    path('book/<int:pk>/delete', book_delete.as_view(), name="book_delete"),
   
   
]

