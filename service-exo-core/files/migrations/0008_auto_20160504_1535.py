# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-05-04 15:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0007_auto_20160503_1144'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='node',
            options={'verbose_name': 'Node', 'verbose_name_plural': 'Nodes'},
        ),
        migrations.AddField(
            model_name='node',
            name='order',
            field=models.IntegerField(blank=True, default=1, null=True),
        ),
    ]