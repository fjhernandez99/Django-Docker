# Generated by Django 3.2.8 on 2021-10-10 02:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0004_alter_usuario_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='role',
            field=models.TextField(default='', max_length=10),
        ),
    ]
