# Generated by Django 3.2.8 on 2021-11-08 23:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0011_auto_20211108_1711'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venta',
            name='cliente',
            field=models.CharField(default='', max_length=50),
        ),
    ]