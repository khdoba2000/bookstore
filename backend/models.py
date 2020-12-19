from django.db import models

from django.core.validators import EmailValidator, MinLengthValidator, RegexValidator
import this
# Create your models here.


class User(models.Model):
    username = models.CharField(max_length=32,
                        validators=[
                            MinLengthValidator(2)
                        ],
                        unique=True)
    password = models.CharField(max_length=32,
                        validators=[
                            MinLengthValidator(2)
                        ],
                        unique=True)
    name = models.CharField(max_length=32,
                        validators=[
                            MinLengthValidator(2)
                        ])
    surname = models.CharField(max_length=32,

                        validators=[
                            MinLengthValidator(2)
                        ])
    email = models.EmailField(validators=[
                            EmailValidator
                        ])
    phone_number = models.CharField(validators=[
                        RegexValidator(regex='^.{9}$', message='Length has to be 9')
                        ],
                        max_length=9)
    def get_books(self):
        return Book.objects.filter(taken_by=self)

    def __str__(self):
        return '"'+self.name+'" with email "'+self.email+'"'

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
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def get_quantity(self):
        quantity = len(Book.objects.filter(model=self))
        return quantity

    def get_books(self):
        return Book.objects.filter(model=self)
    
    def has_book(self):
        for book in self.get_books():
            if book.is_taken==False:
                return True
        return False
            
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
    is_taken = models.BooleanField(default=False)
    taken_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True, blank=True, related_name="books")
    model = models.ForeignKey(Book_model, on_delete=models.CASCADE, related_name="books")

    taken_at = models.DateTimeField(auto_now=True)
    released_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def set_taken(self):
        self.is_taken=True
        
    def release(self):
        self.is_taken=False

    def __str__(self):
        return '"'+self.model.title+'" with code "'+self.code+'"'
    
