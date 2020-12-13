from django.contrib import admin
from .models import Book_model, Book
# Register your models here.
admin.site.register(Book_model)
admin.site.register(Book)