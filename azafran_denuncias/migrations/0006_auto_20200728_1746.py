# Generated by Django 3.0.6 on 2020-07-28 22:46

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('azafran_denuncias', '0005_auto_20200728_1744'),
    ]

    operations = [
        migrations.AlterField(
            model_name='denuncia',
            name='ip_publica_testimonio',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
    ]
