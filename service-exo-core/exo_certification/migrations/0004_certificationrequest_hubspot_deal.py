# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2019-08-28 12:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exo_certification', '0003_merge_20190826_0854'),
    ]

    operations = [
        migrations.AddField(
            model_name='certificationrequest',
            name='hubspot_deal',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]