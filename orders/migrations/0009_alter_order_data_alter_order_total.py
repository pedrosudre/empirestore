# Generated by Django 4.1.3 on 2022-11-26 17:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0008_order_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='data',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 26, 14, 15, 29, 252068)),
        ),
        migrations.AlterField(
            model_name='order',
            name='total',
            field=models.FloatField(default=0.0),
        ),
    ]
