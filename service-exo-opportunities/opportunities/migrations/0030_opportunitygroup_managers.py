# Generated by Django 2.2.7 on 2019-11-08 08:38

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('opportunities', '0029_merge_20191108_0838'),
    ]

    operations = [
        migrations.AddField(
            model_name='opportunitygroup',
            name='managers',
            field=models.ManyToManyField(related_name='manager_groups', to=settings.AUTH_USER_MODEL),
        ),
    ]
