# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2019-08-21 11:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0067_merge_20190717_2101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='category',
            field=models.CharField(choices=[('T', 'Training'), ('C', 'Certification'), ('CC', 'Certification Consultant'), ('CX', 'Certification Sprint Coach'), ('D', 'Demo'), ('E', 'Event'), ('M', 'Transformation')], default='M', max_length=2),
        ),
    ]
