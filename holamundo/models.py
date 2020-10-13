from django.db import models

# Create your models here.
class Carrera(models.Model):
    nombreCarrera=models.CharField(max_length=200)
    numeroCiclo=models.IntegerField(default=5)
    numeroCreditos=models.IntegerField(default=120)
    codigoCarrera=models.CharField(max_length=10)
    numeroDocentes=models.IntegerField(default=5)

class Paralelo(models.Model):
    carrera=models.ForeignKey(Carrera,on_delete=models.CASCADE)
    ciclo=models.IntegerField(default=0)
    nombre=models.CharField(max_length=10)
    numeroEstudiantes=models.IntegerField(default=0)

class Estudiante(models.Model):
    Cedula=models.CharField(max_length=10)
    Nombre=models.CharField(max_length=200)
    Apellido=models.CharField(max_length=200)
    Edad=models.IntegerField(default=2)
    # Carrera=models.ForeignKey(Carrera,on_delete=models.CASCADE)
    # Paralelo=models.ForeignKey(Paralelo,on_delete=models.CASCADE)
    Telefono=models.CharField(max_length=10)
    email=models.CharField(max_length=200)
    direccion=models.CharField(max_length=200)
    Ocupaciones=models.CharField(max_length=200)