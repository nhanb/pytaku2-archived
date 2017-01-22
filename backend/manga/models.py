from django.db import models


class Title(models.Model):
    name = models.CharField(blank=False)
    url = models.URLField(unique=False, blank=False)
    description = models.TextField()


class Chapter(models.Model):
    name = models.CharField(blank=False)
    url = models.URLField(unique=False, blank=False)
    title = models.ForeignKey(Title,
                              related_name='chapters',
                              on_delete=models.CASCADE)
