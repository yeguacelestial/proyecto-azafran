# Generated by Django 3.0.6 on 2020-07-27 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('azafran_denuncias', '0016_auto_20200727_1744'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='denuncia',
            name='user_agent_testimonio',
        ),
        migrations.AlterField(
            model_name='denuncia',
            name='ip_testimonio',
            field=models.CharField(default='127.0.0.1', max_length=100),
        ),
    ]