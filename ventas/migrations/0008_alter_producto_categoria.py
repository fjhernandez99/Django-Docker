# Generated by Django 3.2.8 on 2021-11-06 00:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0007_auto_20211103_1326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='categoria',
            field=models.CharField(choices=[('Consola', 'Consola'), ('Accesorio', 'Accesorio'), ('Juegos', 'Juegos'), ('Membresías', 'Membresías')], default='Consolas', max_length=10),
        ),
    ]
