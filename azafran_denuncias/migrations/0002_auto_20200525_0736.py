# Generated by Django 3.0.6 on 2020-05-25 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        # ('azafran_denuncias', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='denuncia',
            name='genero',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='edad',
            name='edad',
            field=models.CharField(max_length=20),
        ),
    ]
