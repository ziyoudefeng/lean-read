# -*- coding: utf-8-*-
from django.db import models


class Book(models.Model):
    bookId = models.AutoField(primary_key=True)
    name = models.CharField('书名', max_length=100)
    author = models.CharField('作者', max_length=100, blank=True)
    cnFile = models.FileField(upload_to='books/', blank=True)
    enFile = models.FileField(upload_to='books/', blank=True)

    def __unicode__(self):
        return self.name
