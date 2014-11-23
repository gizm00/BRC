from django.db import models


class rssFeed(models.Model):
    title = models.CharField(max_length=200)
    summary = models.CharField(max_length=200
    link = models.CharField('date published')
    author = models.CharField(max_length=200)
    category = models.CharField(max_length=200)

