from django.shortcuts import render
from django.http import HttpResponse
from backend.models import Book
from django.views.generic import ListView
# Create your views here.
app_name = 'frontend'
class book_list(ListView):
    model = Book
    template_name="frontend/list_books.html"



