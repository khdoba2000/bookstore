from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from backend.models import Book_model as Book, User
from django.views.generic import ListView
from django.views import View
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from django.utils import timezone
# Create your views here.
app_name="frontend"

class login(View):
    def get(self, request, pk):
        book_model_id=pk
        return render(request, "frontend/login.html", {'book_id': book_model_id})

    def post(self, request, pk):
        username=request.POST.get('username')
        password=request.POST.get('password')
        for user in User.objects.all():
           if (user.username==username and user.password==password):
                user_id=user.id
                return book_order(request, pk, user_id)
        
        return render(request, "frontend/login.html", {"book_id": pk, "message": "Invalid credantial"}) 
        

class signup(CreateView):
    model=User
    fields="__all__"
    success_url=reverse_lazy("frontend:book_list")
    template_name="frontend/signup.html"


def book_list(request):
    model = Book
    ctx={
        'book_model_list': Book.objects.all()
    }
    template_name = "frontend/book_list.html"
    return render(request, template_name, ctx)
 
def book_order(request, pk, user_id):
        
        book_model=Book.objects.get(pk=pk)
        has_book = book_model.has_book()
        if has_book:
            print(f"Book{pk} ordered")
            available_book=book_model.books.filter(is_taken=False).last()
            print(available_book.code)
            user=User.objects.get(pk=user_id)
            available_book.set_taken()
            available_book.taken_by = user
            available_book.taken_at = timezone.now()
            available_book.save()

            ctx={
                'pk': pk,
                'book': book_model,
                'code': available_book.code,
                'user': user
            }
            template_name = "frontend/order_success.html"
            return render(request, template_name, ctx)
        return render(request, "frontend/no_book_available.html")

def book_release(request, pk, user_id, code):
        
        book_model=Book.objects.get(pk=pk)
        has_book = book_model.has_book()
        if has_book:
            print(f"Book{pk} released")
            book_to_release=book_model.books.filter(code=code)
            print(book_to_release.code)
            user=User.objects.get(pk=user_id)
            book_to_release.release()
            book_to_release.taken_by = None
            book_to_release.released_at = timezone.now()
            book_to_release.save()

            ctx={
                'pk': pk,
                'book': book_model,
                'code': book_to_release.code,
                'user': user
            }
            template_name = "frontend/release_success.html"
            return render(request, template_name, ctx)
        return render(request, "frontend/no_book_available.html")
