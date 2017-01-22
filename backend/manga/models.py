from django.db import models
from django.contrib.postgres.fields import ArrayField


class Title(models.Model):
    name = models.CharField(max_length=300, blank=False)
    url = models.URLField(unique=True, blank=False)
    status = models.CharField(max_length=50, blank=False)
    thumb_url = models.URLField(blank=False)
    authors = ArrayField(models.CharField(max_length=100))
    descriptions = ArrayField(models.TextField())
    tags = ArrayField(models.CharField(max_length=100))
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Chapter(models.Model):
    name = models.CharField(max_length=300, blank=False)
    url = models.URLField(unique=True, blank=False)
    pages = ArrayField(models.CharField(max_length=300), null=True)
    title = models.ForeignKey(Title,
                              related_name='chapters',
                              on_delete=models.CASCADE)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
