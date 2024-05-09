from django.shortcuts import render
from .models import Book

def home(request):

    books = Book.objects.all()

    context = {
        'books': books
    }

    return render(request, 'index.html', context)