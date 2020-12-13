
from django.conf.urls import url
from . import views
from django.shortcuts import get_object_or_404
from django.urls import include, path
from .views import inc, dec, book_model_list, book_model_create, book_model_detail, book_model_update, book_model_delete
app_name = 'backend'

urlpatterns = [
    path('', book_model_list.as_view(), name="book_model_list"),
    path('create', book_model_create.as_view(), name="book_model_create"),
    path('book_model/<int:pk>', book_model_detail.as_view(), name="book_model_detail"),
    path('book_model/<int:pk>/update', book_model_update.as_view(), name="book_model_update"),
    path('book_model/<int:pk>/delete', book_model_delete.as_view(), name="book_model_delete"),
    path('book_model_inc/<int:pk>', inc.as_view(), name='book_model_inc'),
    path('book_model_dec/<int:pk>', dec.as_view(), name="book_model_dec"),   
   
]

