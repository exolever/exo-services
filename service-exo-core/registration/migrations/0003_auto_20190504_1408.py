# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2019-05-04 14:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0002_auto_20190503_1014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stepoption',
            name='post_step',
            field=models.NullBooleanField(),
        ),
        migrations.AlterField(
            model_name='stepoption',
            name='pre_step',
            field=models.NullBooleanField(),
        ),
    ]