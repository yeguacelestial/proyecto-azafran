# Generated by Django 3.0.6 on 2020-07-27 20:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('azafran_denuncias', '0010_denuncia_testimonio_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='denuncia',
            name='testimonio_date',
        ),
    ]