# -*- coding: utf-8-*-
from django.contrib import admin
from bookStore.models import Book, Chapter, ReadingLog, ReadingStatus


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'cnFile', 'enFile')


class ChapterAdmin(admin.ModelAdmin):
    list_display = ('book', 'chapNo', 'chapName', 'abstract')


class ReadingStatusAdmin(admin.ModelAdmin):
    list_display = ('name', 'desc')


class ReadingLogAdmin(admin.ModelAdmin):
    list_display = ('chapter', 'reader', 'status', 'commit', 'notes')


admin.site.register(Book, BookAdmin)
admin.site.register(Chapter, ChapterAdmin)
admin.site.register(ReadingStatus, ReadingStatusAdmin)
admin.site.register(ReadingLog, ReadingLogAdmin)
