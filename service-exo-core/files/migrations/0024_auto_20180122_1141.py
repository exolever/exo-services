# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-01-22 11:41
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0023_auto_20170710_0917'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resource',
            name='metadata',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True),
        ),
    ]
