# Generated by Django 4.1.3 on 2022-11-28 00:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('aplic', '0002_funcionario'),
    ]

    operations = [
        migrations.AddField(
            model_name='funcionario',
            name='user',
            field=models.OneToOneField(default=0, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
