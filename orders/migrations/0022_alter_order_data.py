# Generated by Django 4.1.3 on 2022-11-28 01:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0021_alter_order_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='data',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 27, 22, 32, 31, 101997)),
        ),
    ]
