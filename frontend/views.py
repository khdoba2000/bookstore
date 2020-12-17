from django.shortcuts import render
from django.http import HttpResponse
from backend.models import Book_model as Book
from django.views.generic import ListView
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

app_name = "frontend"
class book_list(ListView):
    model = Book
    template_name = "frontend/book_list.html"
 
class book_order(LoginRequiredMixin, View):
    def get(self, request, pk):
        print(f"Book{pk} ordered")
        return HttpResponse("ORDERED")
    


