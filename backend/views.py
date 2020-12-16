from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from .models import Book_model, Book
from django.views import View
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.


class book_model_list(LoginRequiredMixin, ListView):
    model = Book_model
    fields="__all__"
    success_url =  reverse_lazy('backend:book_model_list')

class book_model_create(LoginRequiredMixin, CreateView):
    model = Book_model
    fields="__all__"
    success_url =  reverse_lazy('backend:book_model_list')


    

class book_model_detail(LoginRequiredMixin,DetailView):
    model = Book_model
    fields="__all__"
    success_url =  reverse_lazy('backend:book_model_list')
  

class book_model_update(LoginRequiredMixin, UpdateView):
    model = Book_model
    fields="__all__"
    success_url =  reverse_lazy('backend:book_model_list')


class book_model_delete(LoginRequiredMixin, DeleteView):
    model = Book_model
    fields="__all__"
    success_url =  reverse_lazy('backend:book_model_list')





class book_list(LoginRequiredMixin, ListView):
    model = Book
    fields="__all__"
    success_url =  reverse_lazy('backend:book_model_list')

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
import json
from backend.models import Book

@method_decorator(csrf_exempt, name='dispatch')

class add_book_set(View):
    def get(self, request):
        num_of_books_to_add=request.GET.get('num', None)
        pk=request.GET.get('pk', None)
        print("NUM= ",num_of_books_to_add)
        print("book_model PK=", pk)
        book_model = get_object_or_404(Book_model, pk=pk)
        print(book_model)
        last_book_in_model=Book.objects.filter(model=book_model).last()
        if last_book_in_model:
            code_of_last=int(last_book_in_model.code)
            if code_of_last+1 <= 999:
               new_code=f"0{code_of_last+1}"
            else:
               new_code=f"{code_of_last+1}"
        else: #if no book is available for the model
            if(book_model.id<10):
                first_2digit=f"0{book_model.id}"
            elif book_model.id<100:
                first_2digit=f"{book_model.id}"
            else:
                return AssertionError
            new_code=f"{first_2digit}00"

        for i in range(int(num_of_books_to_add)):
            new_book=Book(code=new_code, model=book_model)
            new_book.save()
            code_of_last = int(new_book.code)
            if code_of_last+1 <= 999:
               new_code=f"0{code_of_last+1}"
            else:
               new_code=f"{code_of_last+1}"
            
        book_model.save()
        resp = json.dumps({
            'quantity': book_model.get_quantity()
        })
        return HttpResponse(resp, content_type="application/json")        



@method_decorator(csrf_exempt, name='dispatch')
class inc(View):
    def post(self, request, pk):
        print(f"book_model PK {pk}")
        book_model = get_object_or_404(Book_model, pk=pk)
        print(book_model)
        last_book_in_model=Book.objects.filter(model=book_model).last()
        if last_book_in_model:
            print(f"LAst book {last_book_in_model}")
            code_of_last=int(last_book_in_model.code)
            if code_of_last+1 <= 999:
               new_code=f"0{code_of_last+1}"
            else:
               new_code=f"{code_of_last+1}"
               print(new_code)
        else: #if no book is available for the model
            if(book_model.id<10):
                first_2digit=f"0{book_model.id}"
            elif book_model.id<100:
                first_2digit=f"{book_model.id}"
            else:
                return AssertionError
            new_code=f"{first_2digit}00"
            print(new_code)

        book=Book(code=new_code, model=book_model)
        book.save()
        print(f"New book {Book.objects.filter(model=book_model).last()}")
        book_model.save()

        resp = json.dumps({
            'quantity': book_model.get_quantity()
        })
        return HttpResponse(resp, content_type="application/json")        

@method_decorator(csrf_exempt, name='dispatch')
class dec(View):
    def post(self, request, pk):
        book_model = get_object_or_404(Book_model, pk=pk)
        num_of_existing_books=len(Book.objects.filter(model=book_model))
       
        if num_of_existing_books>0:
                last_book_in_model=Book.objects.filter(model=book_model)[num_of_existing_books-1]
                code_of_last=int(last_book_in_model.code)
                last_book_in_model.delete()
        
        else: #if no book in database
            message="No any book_models left in the store"
            resp = json.dumps({
                'message': message,
                'error': True
            })
            return HttpResponse(resp, content_type="application/json")
        print("book_model PK", pk)
        print(book_model)
        resp = json.dumps({
            'quantity': book_model.get_quantity()
        })
        book_model.save()

        return HttpResponse(resp, content_type="application/json")

