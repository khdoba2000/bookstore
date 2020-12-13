from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from .models import Book
from django.views import View
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.


class book_list(LoginRequiredMixin, ListView):
    model = Book
    fields="__all__"
    success_url =  reverse_lazy('backend:book_list')

class book_create(LoginRequiredMixin, CreateView):
    model = Book
    fields="__all__"
    success_url =  reverse_lazy('backend:book_list')
    

class book_detail(LoginRequiredMixin,DetailView):
    model = Book
    fields="__all__"
    success_url =  reverse_lazy('backend:book_list')

class book_update(LoginRequiredMixin, UpdateView):
    model = Book
    fields="__all__"
    success_url =  reverse_lazy('backend:book_list')


class book_delete(LoginRequiredMixin, DeleteView):
    model = Book
    fields="__all__"
    success_url =  reverse_lazy('backend:book_list')


from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.db.utils import IntegrityError

@method_decorator(csrf_exempt, name='dispatch')
class inc(View):
    def post(self, request, pk):
        print("Book PK", pk)
       # book = (Book, pk)
      #  print(book)
        #book.save()
        return HttpResponse()
        

@method_decorator(csrf_exempt, name='dispatch')
class dec(View):
    def post(self, request, pk):
       # book = get_object_or_404(Book,pk)

        #book.quantity = book.quantity + 1
        #book.save()
        print("Book PK", pk)
        #print(book)
        return HttpResponse()

