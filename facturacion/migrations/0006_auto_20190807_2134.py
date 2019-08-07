# Generated by Django 2.2.3 on 2019-08-07 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0006_auto_20190726_0134'),
        ('facturacion', '0005_auto_20190806_0121'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='factura',
            name='productos',
        ),
        migrations.AddField(
            model_name='factura',
            name='productos',
            field=models.ManyToManyField(to='inventario.Producto'),
        ),
    ]