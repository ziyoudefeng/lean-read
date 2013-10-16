# -*- coding: utf-8-*-
from django.db import models
from django.contrib.auth.models import User
import datetime


class Book(models.Model):
    bookId = models.AutoField(primary_key=True)
    title = models.CharField('书名', max_length=100)
    cnFile = models.FileField(upload_to='books/', blank=True)
    enFile = models.FileField(upload_to='books/', blank=True)

    def chapters(self):
        return self.chapter_set.order_by('chapNo')

    def __unicode__(self):
        return self.title


class Chapter(models.Model):
    chapId = models.AutoField(primary_key=True)
    book = models.ForeignKey(Book)
    chapNo = models.IntegerField('章节序号')
    chapName = models.CharField('章节名', max_length=100, blank=True)
    abstract = models.CharField('内容简介', max_length=500, blank=True)

    def __unicode__(self):
        return '%s-Chap %s' % (self.book, self.chapNo)


class ReadingLog(models.Model):
    chapter = models.ForeignKey(Chapter)
    reader = models.ForeignKey(User)
    mark = models.IntegerField('评分')
    notes = models.CharField('评论', max_length=500, blank=True)
    timestamp = models.DateTimeField('时间', default=datetime.datetime.now)
