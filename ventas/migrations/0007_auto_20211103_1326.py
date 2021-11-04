# Generated by Django 3.2.8 on 2021-11-03 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0006_alter_producto_inventario'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='inventario',
        ),
        migrations.AddField(
            model_name='producto',
            name='inventario_pradera',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='producto',
            name='inventario_roosevelt',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
