from django.db import models

# Create your models here.

genre_options=(
    ('science', "science"),
    ('religious', "religious"),
    ('fiction', "fiction"),
    ('biography', "biography")
)
class Book(models.Model):
    title = models.CharField(max_length=64, unique=True)
    author = models.CharField(max_length=64)
    price = models.PositiveIntegerField()
    genre = models.CharField(max_length=64, choices=genre_options)
    quantity = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def inc(self):
        self.quantity = self.quantity + 1

    def __str__(self):
        return self.title+" by "+self.author
    
