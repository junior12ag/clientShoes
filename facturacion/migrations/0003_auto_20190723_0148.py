# Generated by Django 2.2.3 on 2019-07-23 01:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facturacion', '0002_auto_20190723_0145'),
    ]

    operations = [
        migrations.RenameField(
            model_name='factura',
            old_name='numero_orden',
            new_name='numero_factura',
        ),
        migrations.AddField(
            model_name='factura',
            name='cliente',
            field=models.CharField(default='', max_length=50),
        ),
    ]