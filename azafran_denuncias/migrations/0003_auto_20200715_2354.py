# Generated by Django 3.0.6 on 2020-07-15 23:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('azafran_denuncias', '0002_auto_20200525_0736'),
    ]

    operations = [
        migrations.AlterField(
            model_name='denuncia',
            name='genero',
            field=models.CharField(choices=[('', 'Selecciona un género'), ('M', 'Masculino'), ('F', 'Femenino'), ('NB', 'No binario'), ('NA', 'Prefiero no decirlo')], max_length=30),
        ),
        migrations.CreateModel(
            name='DenunciaRecibida',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genero', models.CharField(choices=[('', 'Selecciona un género'), ('M', 'Masculino'), ('F', 'Femenino'), ('NB', 'No binario'), ('NA', 'Prefiero no decirlo')], max_length=30)),
                ('denuncia', models.CharField(max_length=10000)),
                ('edad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='azafran_denuncias.Edad')),
                ('escuela', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='azafran_denuncias.Escuela')),
            ],
        ),
    ]
