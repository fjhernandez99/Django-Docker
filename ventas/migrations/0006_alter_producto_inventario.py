# Generated by Django 3.2.8 on 2021-11-03 00:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0005_auto_20211102_1651'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='inventario',
            field=models.PositiveIntegerField(default=''),
        ),
    ]
