# Generated by Django 2.2.4 on 2019-08-26 14:48

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('learning', '0013_auto_20190307_1144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermicrolearning',
            name='responses',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=list, null=True),
        ),
    ]
