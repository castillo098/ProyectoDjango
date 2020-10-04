from django.db import models

# Create your models here.
class Carrera(models.Model):
    nombreCarrera=models.CharField(max_length=200,default="N/A")
    numeroCiclo=models.IntegerField(default=5)
    numeroCreditos=models.IntegerField(default=120)
    codigoCarrera=models.CharField(max_length=10,default="N/A")
    numeroDocentes=models.IntegerField(default=5)

class Paralelo(models.Model):
    carrera=models.ForeignKey(Carrera,on_delete=models.CASCADE,default=None)
    ciclo=models.IntegerField(default=5)
    nombre=models.CharField(max_length=10,default="N/A")
    numeroEstudiantes=models.IntegerField(default=5)