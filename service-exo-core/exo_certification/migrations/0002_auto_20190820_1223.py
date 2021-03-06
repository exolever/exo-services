# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2019-08-20 12:23
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('exo_certification', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='coupon',
            name='expiry_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='coupon',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='referral_codes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='coupon',
            name='type',
            field=models.CharField(choices=[('A', 'Fixed Amount'), ('P', 'Percent')], default='A', max_length=1),
        ),
    ]
