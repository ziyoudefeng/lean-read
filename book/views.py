#-*- coding:utf-8 -*-
from django.shortcuts import render_to_response
from book.models import Book
from django.conf import settings


def overview(request):
    content = {'MEDIA_URL': settings.MEDIA_URL,
               'books': Book.objects.all()
               }
    return render_to_response('book_list.html', content)
