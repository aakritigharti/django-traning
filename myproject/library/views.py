from django.shortcuts import render

# Create your views hefrom django.shortcuts import render
from .models import Author, Book

def book_list(request):
    books = Book.objects.all()
    return render(request, "library/book_list.html", {"books": books})
