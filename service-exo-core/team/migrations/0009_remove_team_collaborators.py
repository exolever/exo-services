# Generated by Django 2.2.8 on 2019-12-18 06:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0008_team_uuid_unique'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team',
            name='collaborators',
        ),
    ]
