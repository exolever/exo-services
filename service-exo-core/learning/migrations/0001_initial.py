# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-06-28 09:45
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields
import utils.models.unique_order


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Resource',
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
                ('name', models.CharField(max_length=150)),
                ('description', models.CharField(blank=True, max_length=200, null=True)),
                ('order', models.IntegerField()),
                ('file', models.FileField(blank=True, null=True, upload_to='resources')),
                ('link', models.CharField(blank=True, max_length=200, null=True)),
                ('active', models.BooleanField(default=True)),
                (
                    'created_by', models.ForeignKey(
                        blank=True, null=True, on_delete=django.db.models.deletion.CASCADE,
                        related_name='learning_resource_related', to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                'verbose_name_plural': 'Resources',
                'permissions': (('list_resource', 'List resources'),),
                'verbose_name': 'Resource',
                'ordering': ['order'],
            },
            bases=(utils.models.unique_order.UniqueOrderMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Tag',
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
                ('name', models.CharField(max_length=200)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.AddField(
            model_name='resource',
            name='tags',
            field=models.ManyToManyField(to='learning.Tag', verbose_name='Tags'),
        ),
        migrations.CreateModel(
            name='TrainingSession',
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
                ('name', models.CharField(max_length=150)),
                ('description', models.CharField(blank=True, max_length=200, null=True)),
                ('date', models.DateField(blank=True, null=True)),
                (
                    'created_by', models.ForeignKey(
                        blank=True, null=True, on_delete=django.db.models.deletion.CASCADE,
                        related_name='learning_trainingsession_related', to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                'abstract': False,
            },
        ),
    ]