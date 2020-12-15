from django.db import models

from django.core.validators import MinLengthValidator, RegexValidator
import this
# Create your models here.

genre_options=(
    ('science', "science"),
    ('religious', "religious"),
    ('fiction', "fiction"),
    ('biography', "biography")
)
class Book_model(models.Model):
    title = models.CharField(
        max_length=64,
        unique=True, 
        validators=[
            MinLengthValidator(3)
        ])
    author = models.CharField(max_length=64)
    price = models.PositiveIntegerField()
    genre = models.CharField(max_length=64, choices=genre_options)
    quantity = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def get_quantity(self):
        self.quantity = len(Book.objects.filter(model=self))
        return self.quantity

    def get_books(self):
        return Book.objects.filter(model=self)

    def __str__(self):
        return '"'+self.title+'" by "'+self.author+'"'
    

class Book(models.Model):
    code = models.CharField(
        validators=[
            RegexValidator(regex='^.{4}$', message='Length has to be 4')
        ],
        max_length=4,
        unique=True
    )
    model = models.ForeignKey(Book_model, on_delete=models.CASCADE, related_name="books")


    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return '"'+self.model.title+'" with code "'+self.code+'"'
    
