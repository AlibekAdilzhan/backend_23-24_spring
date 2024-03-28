from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from books.models import Book


def books(request):
    template = loader.get_template("all_books.html")
    all_books = Book.objects.all().values()
    my_context = {
        "all_books": all_books
    }
    return HttpResponse(template.render(context=my_context))