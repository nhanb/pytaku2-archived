from django.db import models
from django.contrib.postgres.fields import ArrayField, JSONField
from django.utils.timezone import now


class Title(models.Model):
    name = models.CharField(max_length=300, blank=False)
    url = models.URLField(unique=True, blank=False)
    status = models.CharField(max_length=50, blank=False)
    thumb_url = models.URLField(blank=False)
    authors = ArrayField(models.CharField(max_length=100))
    descriptions = ArrayField(models.TextField())
    tags = ArrayField(models.CharField(max_length=100))
    last_updated = models.DateTimeField(auto_now=True)
    chapters = JSONField()

    def __str__(self):
        return self.name

    def is_old(self):
        return (now() - self.last_updated).days >= 1


class Chapter(models.Model):
    url = models.URLField(unique=True, blank=False)
    name = models.CharField(max_length=300, blank=False)
    pages = ArrayField(models.CharField(max_length=300), default=[])
    last_updated = models.DateTimeField(auto_now=True)

    title = models.ForeignKey(Title, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    @property
    def is_old(self):
        return (now() - self.last_updated).days >= 1
