from django.db import models
from django import forms

# Create your models here.

# Modelo de denuncias recibidas
class Denuncia(models.Model):
    GENEROS = (
        ('', 'Selecciona un género'),
        ('Masculino', 'Masculino'),
        ('Femenino', 'Femenino'),
        ('No binario', 'No binario'),
        ('No especificado', 'Prefiero no decirlo')
    )

    EDADES = (
        ('', 'Selecciona un rango de edad'),
        ('De 5 a 10 años', 'De 5 a 10 años'),
        ('De 11 a 15 años', 'De 11 a 15 años'),
        ('De 16 a 20 años', 'De 16 a 20 años'),
        ('De 21 a 25 años', 'De 21 a 25 años'),
        ('De 26 a 30 años', 'De 26 a 30 años'),
        ('Más de 30 años', 'Más de 30 años')
    )

    edad = models.CharField(max_length=30, choices=EDADES)
    genero = models.CharField(max_length=30, choices=GENEROS)
    denuncia = models.CharField(max_length=10000)
    testimonio_fecha = models.DateTimeField(auto_now_add=True)

    # Info from user
    ip_publica_testimonio = models.GenericIPAddressField()


# Modelo de denuncias publicadas
class DenunciaPublicada(models.Model):
    denuncia = models.CharField(max_length=10000)

    HASHTAGS = (
        '#YoTeCreo',
        '#MeTooMX',
        '#NoEstasSolx',
        '#NiUnaMas',
        '#NoAlAcoso',
        '#MeTooEATA'
    )