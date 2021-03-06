# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-07-03 06:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ExOAttribute',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                (
                    'created', model_utils.fields.AutoCreatedField(
                        default=django.utils.timezone.now, editable=False, verbose_name='created',
                    ),
                ),
                (
                    'modified', model_utils.fields.AutoLastModifiedField(
                        default=django.utils.timezone.now, editable=False, verbose_name='modified',
                    ),
                ),
                ('name', models.CharField(max_length=100)),
                ('_type', models.CharField(choices=[('S', 'Scale'), ('I', 'Ideas')], max_length=1)),
                ('order', models.IntegerField()),
            ],
            options={
                'verbose_name': 'ExOAttribute',
                'ordering': ['order'],
                'verbose_name_plural': 'ExOAttributes',
            },
        ),
    ]
