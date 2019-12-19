# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2019-03-13 09:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zoom_project', '0001_squashed_0015_auto_20170710_0717'),
    ]

    operations = [
        migrations.AddField(
            model_name='zoomroom',
            name='zoom_id',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='Internal Meeting ID (Zoom)'),
        ),
    ]