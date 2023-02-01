# Generated by Django 4.1.5 on 2023-02-01 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_riderequestinfo_owner_alter_riderequestinfo_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='riderequestinfo',
            name='owner',
        ),
        migrations.AlterField(
            model_name='riderequestinfo',
            name='status',
            field=models.CharField(choices=[('COMPLETE', 'COMPLETE'), ('OPEN', 'OPEN'), ('COMFIRM', 'COMFIRM')], default='OPEN', max_length=20),
        ),
    ]