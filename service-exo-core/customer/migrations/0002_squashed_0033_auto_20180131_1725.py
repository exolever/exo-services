# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-02-01 10:02
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
        ('relation', '0001_squashed_0040_consultantactivity'),
        ('exo_accounts', '__first__'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('partner', '0001_squashed_0010_auto_20170523_0748'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customer',
            options={
                'ordering': ['name'], 'permissions': (
                    ('edit_customer', 'Edit Customer information'),
                    ('add_user', 'Add user role'),
                    ('remove_customer', 'Remove Customer'),
                    ('view_customer', 'View General Customer information'),
                    ('list_customer', 'List customer'),
                ), 'verbose_name': 'Client', 'verbose_name_plural': 'Clients',
            },
        ),
        migrations.AddField(
            model_name='customer',
            name='users',
            field=models.ManyToManyField(
                related_name='customers',
                through='relation.CustomerUserRole', to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name='customer',
            name='partners',
            field=models.ManyToManyField(
                related_name='customers',
                through='relation.PartnerCustomerRole', to='partner.Partner',
            ),
        ),
    ]