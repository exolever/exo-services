# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-05-20 10:01
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sprint', '0018_merge'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sprint',
            options={'ordering': ['name'], 'verbose_name': 'Sprint', 'verbose_name_plural': 'Sprints'},
        ),
    ]
