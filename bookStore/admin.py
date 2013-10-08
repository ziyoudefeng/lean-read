# -*- coding: utf-8-*-
from django.contrib import admin
from bookStore.models import Book, Chapter, ReadingLog


class BookAdmin(admin.ModelAdmin):
    list_display = ('name', 'cnFile', 'enFile')


class ChapterAdmin(admin.ModelAdmin):
    list_display = ('book', 'chapNo', 'chapName')


class ReadingLogAdmin(admin.ModelAdmin):
    list_display = ('chapter', 'reader', 'mark', 'notes')


admin.site.register(Book, BookAdmin)
admin.site.register(Chapter, ChapterAdmin)
admin.site.register(ReadingLog, ReadingLogAdmin)
