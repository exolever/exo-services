# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-06-13 09:01
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion

from ..models.user_microlearning import UserMicroLearning


def link_teams_for_user_microlearning(apps, schema_editor):
    for user_microlearning in UserMicroLearning.objects.all():
        team = user_microlearning.user.teams.filter(
            project=user_microlearning.project).first()
        if not team:
            team = user_microlearning.project.teams.filter(
                coach__user=user_microlearning.user).first()

        user_microlearning.team = team
        user_microlearning.save()


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0002_auto_20180424_0757'),
        ('learning', '0011_auto_20180227_1035'),
    ]

    operations = [
        migrations.AddField(
            model_name='usermicrolearning',
            name='team',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE,
                                    related_name='microlearnings_responses', to='team.Team'),
        ),
        migrations.AlterField(
            model_name='usermicrolearning',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                    related_name='microlearnings', to=settings.AUTH_USER_MODEL),
        ),
        migrations.RunPython(link_teams_for_user_microlearning),
    ]
