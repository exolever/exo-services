# Generated by Django 2.2.7 on 2019-11-19 09:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('opportunities', '0030_auto_20191112_1637'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='applicantsow',
            name='role',
        ),
        migrations.RemoveField(
            model_name='applicantsow',
            name='role_code',
        ),
        migrations.RemoveField(
            model_name='opportunity',
            name='old_duration',
        ),
        migrations.RemoveField(
            model_name='opportunity',
            name='role',
        ),
        migrations.RemoveField(
            model_name='opportunity',
            name='role_code',
        ),
    ]