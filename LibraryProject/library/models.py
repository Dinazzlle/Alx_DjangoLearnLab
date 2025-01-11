from django.db import models

# Create your models here.
from library.models import Book

# Create
book = Book.objects.create(title="Django for Beginners", author="William S. Vincent", published_date="2023-01-01", isbn="1234567890123")

# Read
books = Book.objects.all()

# Update
book.title = "Advanced Django"
book.save()

# Delete
book.delete()


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    published_date = models.DateField()
    isbn = models.CharField(max_length=13)

    def __str__(self):
        return self.title
