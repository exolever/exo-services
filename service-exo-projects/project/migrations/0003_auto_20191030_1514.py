# Generated by Django 2.2.6 on 2019-10-30 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_projectrole_exo_role'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectsettings',
            name='feedback',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='projectsettings',
            name='quizes',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='projectsettings',
            name='swarm_session',
            field=models.BooleanField(default=False),
        ),
    ]
