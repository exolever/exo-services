# Generated by Django 2.2.5 on 2019-09-11 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('opportunities', '0022_merge_20190909_1459'),
    ]

    operations = [
        migrations.AddField(
            model_name='applicantfeedback',
            name='status',
            field=models.CharField(blank=True, choices=[('D', 'Done'), ('N', 'Not completed')], max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='opportunity',
            name='_status',
            field=models.CharField(choices=[('X', 'Draft'), ('R', 'Requested'), ('M', 'Removed'), ('L', 'Closed')], default='X', max_length=1),
        ),
        migrations.AlterField(
            model_name='opportunitystatus',
            name='status',
            field=models.CharField(choices=[('X', 'Draft'), ('R', 'Requested'), ('M', 'Removed'), ('L', 'Closed')], default='X', max_length=1),
        ),
    ]