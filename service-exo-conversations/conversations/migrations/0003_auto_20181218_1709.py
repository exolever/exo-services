# Generated by Django 2.1.4 on 2018-12-18 17:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('conversations', '0002_auto_20181213_1102'),
    ]

    operations = [
        migrations.RenameField(
            model_name='conversation',
            old_name='uuid',
            new_name='uuid_related_object',
        ),
    ]