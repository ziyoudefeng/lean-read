# -*- coding: utf-8-*-
from django.db import models
from django.contrib.auth.models import User
import datetime


class Book(models.Model):
    bookId = models.AutoField(primary_key=True)
    name = models.CharField('书名', max_length=100)
    author = models.CharField('作者', max_length=100, blank=True)
    cnFile = models.FileField(upload_to='books/', blank=True)
    enFile = models.FileField(upload_to='books/', blank=True)

    def __unicode__(self):
        return self.name


class Chapter(models.Model):
    chapId = models.AutoField(primary_key=True)
    book = models.ForeignKey(Book)
    chapNo = models.IntegerField('章节序号')
    chapName = models.CharField('章节名', max_length=100, blank=True)

    def __unicode__(self):
        return '%s-Chap %s' % (self.book, self.chapNo)


class ReadingLog(models.Model):
    chapter = models.ForeignKey(Chapter)
    reader = models.ForeignKey(User)
    mark = models.IntegerField('评分')
    notes = models.CharField('评论', max_length=500, blank=True)
    timestamp = models.DateTimeField('时间', default=datetime.datetime.now)
