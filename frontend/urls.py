
from django.conf.urls import url
from . import views
app_name='frontend'

urlpatterns = [
    url("", views.book_list.as_view(), name="book_list"),
   
]

