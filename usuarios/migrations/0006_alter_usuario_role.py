# Generated by Django 3.2.8 on 2021-10-10 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0005_usuario_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='role',
            field=models.CharField(default='', max_length=10),
        ),
    ]
