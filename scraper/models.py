from django.db import models


class BlogCorpus(models.Model):
    time = models.DateField()   
    title = models.CharField(max_length=200)
    summary = models.CharField(max_length=200)
    link = models.IPAddressField(max_length=100)
    author = models.CharField(max_length=200)
    category = models.CharField(max_length=200)

