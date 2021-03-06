# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-16 08:27
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sprint', '0028_auto_20161223_0823'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='coach',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name='teams_coach_old', to='consultant.Consultant', verbose_name='ExO Coach',
            ),
        ),
        migrations.AlterField(
            model_name='team',
            name='sprint',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name='teams_old', to='sprint.Sprint',
            ),
        ),
        migrations.AlterField(
            model_name='team',
            name='team_members',
            field=models.ManyToManyField(blank=True, related_name='teams_old', to=settings.AUTH_USER_MODEL),
        ),
    ]
