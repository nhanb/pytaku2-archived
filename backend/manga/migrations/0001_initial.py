# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-04 06:46
from __future__ import unicode_literals

import django.contrib.postgres.fields
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chapter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(unique=True)),
                ('name', models.CharField(max_length=300)),
                ('pages', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=300), default=[], size=None)),
                ('last_updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Title',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('url', models.URLField(unique=True)),
                ('status', models.CharField(max_length=50)),
                ('thumb_url', models.URLField()),
                ('authors', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=100), size=None)),
                ('descriptions', django.contrib.postgres.fields.ArrayField(base_field=models.TextField(), size=None)),
                ('tags', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=100), size=None)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('chapters', django.contrib.postgres.fields.jsonb.JSONField()),
            ],
        ),
        migrations.AddField(
            model_name='chapter',
            name='title',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manga.Title'),
        ),
    ]
