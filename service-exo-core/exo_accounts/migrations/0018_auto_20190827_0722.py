# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2019-08-27 07:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exo_accounts', '0017_auto_20190818_1511'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_title',
            field=models.TextField(blank=True, null=True),
        ),
    ]