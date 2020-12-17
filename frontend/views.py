from django.shortcuts import render
from django.http import HttpResponse
from backend.models import Book_model as Book
from django.views.generic import ListView
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
app_name="frontend"
def book_list(request):
    model = Book
    ctx={
        'book_model_list': Book.objects.all()
    }
    template_name = "frontend/book_list.html"
    return render(request, template_name, ctx)
 
def book_order(request, pk):
        print(f"Book{pk} ordered")
        book_model=Book.objects.get(pk=pk)
        if book_model.get_quantity():
            code=book_model.books.last().code
            book_model.delete()
            
        ctx={
            'pk': pk,
            'book': book_model,
            'code': code
        }
        template_name="frontend/order_success.html"
        return render(request, template_name, ctx)
