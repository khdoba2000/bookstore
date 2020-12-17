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
        has_book = book_model.has_book()
        if has_book:
            available_book=book_model.books.filter(is_taken=False).last()
            print(available_book.code)
            available_book.set_taken()
            available_book.save()

            ctx={
                'pk': pk,
                'book': book_model,
                'code': available_book.code
            }
            template_name="frontend/order_success.html"
            return render(request, template_name, ctx)
        return render(request, "frontend/no_book_available.html")
