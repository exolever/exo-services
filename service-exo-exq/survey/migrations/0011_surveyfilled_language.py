# Generated by Django 2.2.6 on 2019-10-07 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0010_survey_language'),
    ]

    operations = [
        migrations.AddField(
            model_name='surveyfilled',
            name='language',
            field=models.CharField(blank=True, default='en', max_length=10, null=True),
        ),
    ]