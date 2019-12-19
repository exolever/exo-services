# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2019-08-23 09:57
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('exo_certification', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='certificationrequest',
            name='level',
            field=models.CharField(choices=[('level_1', 'ExO Foundations'), ('level_2', 'Exponential Organizations'), ('level_2_ft', 'Exponential Organizations Fastrack'), ('level_3', 'Exponential Transformation')], default='level_2', max_length=10),
        ),
        migrations.AddField(
            model_name='certificationrequest',
            name='requester_email',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='certificationrequest',
            name='requester_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='certificationrequest',
            name='cohort',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='certification_requests', to='exo_certification.CertificationCohort'),
        ),
        migrations.AlterField(
            model_name='certificationrequest',
            name='price',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='certificationrequest',
            name='status',
            field=models.CharField(choices=[('D', 'Draft'), ('P', 'Pending'), ('A', 'Paid'), ('F', 'Completed'), ('C', 'Cancelled')], default='D', max_length=1),
        ),
        migrations.AlterField(
            model_name='certificationrequest',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='certification_request', to=settings.AUTH_USER_MODEL),
        ),
    ]