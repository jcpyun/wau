# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-25 03:16
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('counter', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clicks',
            name='beer',
        ),
        migrations.RemoveField(
            model_name='clicks',
            name='name',
        ),
        migrations.AddField(
            model_name='clicks',
            name='content',
            field=models.TextField(default=datetime.datetime(2016, 1, 25, 3, 16, 33, 527819, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='clicks',
            name='title',
            field=models.CharField(default=datetime.datetime(2016, 1, 25, 3, 16, 41, 519067, tzinfo=utc), max_length=120),
            preserve_default=False,
        ),
    ]
