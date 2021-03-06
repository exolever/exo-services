# Generated by Django 2.2.6 on 2019-10-31 15:17

from django.db import migrations, models
import relation.managers.customer_user
import relation.managers.partner_user


class Migration(migrations.Migration):

    dependencies = [
        ('relation', '0014_auto_20191028_0826'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='partneruserrole',
            options={'permissions': (('active_role', 'Can activate a role'), ('cancel_role', 'Can cancel a role')), 'verbose_name': 'Partner User', 'verbose_name_plural': 'Partner Users'},
        ),
        migrations.AlterModelManagers(
            name='customeruserrole',
            managers=[
                ('objects', relation.managers.customer_user.CustomerUserRoleManager()),
            ],
        ),
        migrations.AlterModelManagers(
            name='partneruserrole',
            managers=[
                ('objects', relation.managers.partner_user.PartnerUserRoleManager()),
            ],
        ),
        migrations.AddField(
            model_name='consultantprojectrole',
            name='exo_role_other_name',
            field=models.CharField(blank=True, max_length=355, null=True),
        ),
        migrations.AddField(
            model_name='userprojectrole',
            name='exo_role_other_name',
            field=models.CharField(blank=True, max_length=355, null=True),
        ),
    ]
