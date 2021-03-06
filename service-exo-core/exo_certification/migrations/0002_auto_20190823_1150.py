# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2019-08-23 11:50
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('exo_certification', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CouponLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(
                    default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(
                    default=django.utils.timezone.now, editable=False, verbose_name='modified')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='coupon',
            name='created',
            field=model_utils.fields.AutoCreatedField(
                default=django.utils.timezone.now, editable=False, verbose_name='created'),
        ),
        migrations.AddField(
            model_name='coupon',
            name='modified',
            field=model_utils.fields.AutoLastModifiedField(
                default=django.utils.timezone.now, editable=False, verbose_name='modified'),
        ),
        migrations.AddField(
            model_name='couponlog',
            name='coupon',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                    related_name='logs', to='exo_certification.Coupon'),
        ),
        migrations.AddField(
            model_name='couponlog',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
