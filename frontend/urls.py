app_name='frontend'
from django.conf.urls import url
from django.urls import include,path
from frontend.views import book_list, book_order


urlpatterns = [
    url("", book_list.as_view(), name="book_list"),
    path("book_order/<int:pk>", book_order.as_view(), name="book_order")
]

