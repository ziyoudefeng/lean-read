#-*- coding:utf-8 -*-
from django.shortcuts import render_to_response
from bookStore.models import Book
from django.conf import settings


def book_list(request):
    content = {'MEDIA_URL': settings.MEDIA_URL,
               'books': Book.objects.all()
               }
    return render_to_response('book_list.html', content)


def book_detail(request, bookId):
    try:
        book = Book.objects.get(bookId=bookId)
    except Book.DoesNotExist:
        book = None
    content = {'MEDIA_URL': settings.MEDIA_URL,
               'book': book
               }
    return render_to_response('book_detail.html', content)
