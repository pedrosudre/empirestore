# Generated by Django 4.1.3 on 2022-11-23 11:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0002_alter_billingprofile_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='billingprofile',
            name='timestamp',
        ),
    ]
