# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-22 18:18
from __future__ import unicode_literals

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manga', '0002_title_thumb_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chapter',
            name='pages',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=300), blank=True, size=None),
        ),
    ]
