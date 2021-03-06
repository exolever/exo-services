# Generated by Django 2.1.7 on 2019-03-26 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conversations', '0008_conversationuser_profile_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conversationuser',
            name='name',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='conversationuser',
            name='profile_picture',
            field=models.URLField(null=True),
        ),
        migrations.AlterField(
            model_name='conversationuser',
            name='profile_url',
            field=models.URLField(default='', null=True),
        ),
        migrations.AlterField(
            model_name='conversationuser',
            name='short_title',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
