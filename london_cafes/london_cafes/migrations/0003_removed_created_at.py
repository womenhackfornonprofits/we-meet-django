# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-03-26 19:21
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('london_cafes', '0002_renamed_ratings_fields'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cafe',
            name='created_at',
        ),
    ]