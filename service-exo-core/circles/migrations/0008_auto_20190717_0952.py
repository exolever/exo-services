# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2019-07-17 09:52
from __future__ import unicode_literals

import django
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('keywords', '0001_squashed_0004_auto_20171031_1102'),
        ('circles', '0007_circle_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='circle',
            name='tags',
            field=models.ManyToManyField(to='keywords.Keyword'),
        ),
        migrations.AddField(
            model_name='circle',
            name='type',
            field=models.CharField(choices=[('O', 'Open'), ('P', 'Public'), ('S', 'Private'), ('C', 'Certified')], default='O', max_length=1),
        ),
        migrations.AddField(
            model_name='circle',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE,
                                    related_name='circles_circle_related', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='circle',
            name='removed',
            field=models.BooleanField(default=False),
        ),
    ]
