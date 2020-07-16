from django.db import models
from django import forms

# Create your models here.

class Escuela(models.Model):
    escuela = models.CharField(max_length=100)

    def __str__(self):
        return self.escuela

class Edad(models.Model):
    edad = models.CharField(max_length=20)

    def __str__(self):
        return self.edad

# class Genero(models.Model):
#     genero = models.CharField(max_length=50)

#     def __str__(self):
#         return self.genero

# Modelo de denuncias recibidas
class Denuncia(models.Model):
    GENEROS = (
        ('', 'Selecciona un género'),
        ('M', 'Masculino'),
        ('F', 'Femenino'),
        ('NB', 'No binario'),
        ('NA', 'Prefiero no decirlo')
    )

    edad = models.ForeignKey(Edad, on_delete=models.CASCADE)
    genero = models.CharField(max_length=30, choices=GENEROS)
    escuela = models.ForeignKey(Escuela, on_delete=models.CASCADE)
    denuncia = models.CharField(max_length=10000)


# Modelo de denuncias publicadas
class DenunciaPublicada(models.Model):
    GENEROS = (
        ('', 'Selecciona un género'),
        ('M', 'Masculino'),
        ('F', 'Femenino'),
        ('NB', 'No binario'),
        ('NA', 'Prefiero no decirlo')
    )

    edad = models.ForeignKey(Edad, on_delete=models.CASCADE)
    genero = models.CharField(max_length=30, choices=GENEROS)
    escuela = models.ForeignKey(Escuela, on_delete=models.CASCADE)
    denuncia = models.CharField(max_length=10000)

