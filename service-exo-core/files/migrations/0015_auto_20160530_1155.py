# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-05-30 11:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('files', '0011_node_exo_projects'),
    ]

    operations = [
        migrations.AddField(
            model_name='node',
            name='owner_content_type',
            field=models.ForeignKey(
                blank=True, null=True, on_delete=django.db.models.deletion.CASCADE,
                related_name='node_owner', to='contenttypes.ContentType',
            ),
        ),
        migrations.AddField(
            model_name='node',
            name='owner_object_id',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
