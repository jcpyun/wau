# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-25 03:19
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('counter', '0002_auto_20160125_0316'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='clicks',
            new_name='click',
        ),
    ]
