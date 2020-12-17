from django.conf.urls import url
from django.urls import include,path
from frontend.views import book_list, book_order

app_name='frontend'

urlpatterns = [
    path("", book_list, name="book_list"),
    path("book_order/<int:pk>", book_order, name="book_order")
]

