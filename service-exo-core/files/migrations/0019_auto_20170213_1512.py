# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-13 15:12
from __future__ import unicode_literals

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0018_auto_20170125_1632'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resource',
            name='slug',
            field=autoslug.fields.AutoSlugField(
                always_update=True, editable=False,
                max_length=200, populate_from='name',
            ),
        ),
    ]
