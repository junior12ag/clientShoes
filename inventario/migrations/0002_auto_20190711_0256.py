# Generated by Django 2.2.3 on 2019-07-11 02:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='color',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='producto',
            name='modelo',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='producto',
            name='size',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
