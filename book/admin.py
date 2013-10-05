# -*- coding: utf-8-*-
from django.contrib import admin
from book.models import Book


class BookAdmin(admin.ModelAdmin):
    list_display = ('name', 'author', 'cnFile', 'enFile')


admin.site.register(Book, BookAdmin)
