# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-05-06 07:22
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0009_auto_20160505_0712'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fileexoproject',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='fileexoproject',
            name='exo_project',
        ),
        migrations.RemoveField(
            model_name='fileexoproject',
            name='file',
        ),
        migrations.RemoveField(
            model_name='node',
            name='exo_projects',
        ),
        migrations.DeleteModel(
            name='FileExOProject',
        ),
    ]