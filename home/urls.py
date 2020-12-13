from django.conf.urls import url
from . import views
from django.shortcuts import get_object_or_404
from django.urls import include, path
from .views import home
app_name = 'home'

urlpatterns = [
    url('', home, name="home"),
    
]