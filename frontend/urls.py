from django.conf.urls import url
from django.urls import include,path
from frontend.views import book_list, book_order, book_release, signup, login

app_name='frontend'

urlpatterns = [
    path("", book_list, name="book_list"),
    path("book_order/<int:pk>", book_order, name="book_order"),
    path("book_release/<int:pk>", book_release, name="book_order"),
    path("signup", signup.as_view(), name="signup"),
    path("login/<int:pk>", login.as_view(), name="login"),

]

