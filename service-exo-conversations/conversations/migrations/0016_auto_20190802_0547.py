# Generated by Django 2.2.3 on 2019-08-02 05:47

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('conversations', '0015_auto_20190801_1839'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conversation',
            name='uuid_related_object',
            field=models.UUIDField(blank=True, default=uuid.uuid4, null=True),
        ),
    ]