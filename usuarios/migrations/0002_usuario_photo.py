# Generated by Django 3.2.8 on 2021-10-09 23:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='photo',
            field=models.ImageField(default='images/deafualt.png', upload_to='foto'),
        ),
    ]
