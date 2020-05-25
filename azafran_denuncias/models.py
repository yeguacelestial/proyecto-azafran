from django.db import models

# Create your models here.

class Escuela(models.Model):
    escuela = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Edad(models.Model):
    edad = models.CharField(max_length=10)

    def __str__(self):
        return self.title

# Formulario de denuncias
class Denuncia(models.Model):
    genero = models.CharField(max_length=20)
    denuncia = models.CharField(max_length=10000)

    edad = models.ForeignKey(Edad, on_delete=models.CASCADE)
    escuela = models.ForeignKey(Escuela, on_delete=models.CASCADE)
