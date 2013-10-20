# -*- coding: utf-8-*-
from django.db import models
from django.contrib.auth.models import User
import datetime


class Book(models.Model):
    bookId = models.AutoField(primary_key=True)
    title = models.CharField(u'书名', max_length=100)
    cnFile = models.FileField(upload_to='books/', blank=True)
    enFile = models.FileField(upload_to='books/', blank=True)

    def chapters(self):
        return self.chapter_set.order_by('chapNo')

    def __unicode__(self):
        return self.title


class Chapter(models.Model):
    chapId = models.AutoField(primary_key=True)
    book = models.ForeignKey(Book)
    chapNo = models.IntegerField(u'章节序号')
    chapName = models.CharField(u'章节名', max_length=100, blank=True)
    abstract = models.CharField(u'内容简介', max_length=500, blank=True)

    def __unicode__(self):
        return u'%s-Chap %s.%s' % (self.book, self.chapNo, self.chapName)


class ReadingStatus(models.Model):
    name = models.CharField(u'阅读状态', max_length=100) 
    desc = models.CharField(u'状态简介', max_length=500) 

    def __unicode__(self):
        return u'%s' %(self.name)


class ReadingLog(models.Model):
    chapter = models.ForeignKey(Chapter)
    reader = models.ForeignKey(User)
    status = models.ForeignKey(ReadingStatus)
    commit = models.CharField(u'评论', max_length=500, blank=True)
    notes = models.CharField(u'笔记', max_length=500, blank=True)
    timestamp = models.DateTimeField(u'时间', default=datetime.datetime.now)

    def __unicode__(self):
        return u'%s-%s-%s' % (self.reader, self.status, self.chapter)
