# Generated by Django 3.2.8 on 2021-11-08 23:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0012_alter_venta_cliente'),
    ]

    operations = [
        migrations.AddField(
            model_name='productoventa',
            name='precio',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6),
        ),
    ]