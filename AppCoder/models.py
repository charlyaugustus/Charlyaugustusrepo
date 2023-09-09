from django.db import models

# Create your models here.
class Curso(models.Model):

    nombre = models.CharField(max_length=40)
    camada = models.IntegerField()
    
    def __str__(self) -> str:
        return f'{self.nombre} - {self.camada}'

class Estudiante(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField()

class Profesores(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField()
    profesion = models.CharField(max_length=40)
    
class Entregables(models.Model):
    nombre = models.CharField(max_length=40)
    fecha_entrega = models.DateField()
    entregado = models.BooleanField()
    link = models.CharField(max_length=256, null=True)