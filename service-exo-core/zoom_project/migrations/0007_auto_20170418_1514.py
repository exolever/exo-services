# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-18 15:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zoom_project', '0006_remove_zoomsettings_project'),
    ]

    operations = [
        migrations.AlterField(
            model_name='zoomroom',
            name='host_meeting_id',
            field=models.TextField(verbose_name='Host Meeting ID (Zoom)'),
        ),
    ]
