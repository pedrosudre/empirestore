# Generated by Django 4.1.3 on 2022-11-28 01:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0015_remove_product_timestamp'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'Produto', 'verbose_name_plural': 'Produtos'},
        ),
    ]
