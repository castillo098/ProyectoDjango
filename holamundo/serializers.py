from holamundo.models import Carrera, Paralelo, Estudiante
from rest_framework import serializers

class CarreraSerializer(serializers.ModelSerializer):
    class Meta: 
        model=Carrera
        fields={
            'nombreCarrera','numeroCiclo','numeroCreditos','codigoCarrera','numeroDocentes'
        }
class ParaleloSerializer(serializers.ModelSerializer):
    class Meta:
        model=Paralelo
        fields={
            'carrera','ciclo','nombre','numeroEstudiantes'
        }
class EstudianteSerializer(serializers.ModelSerializer):
    class Meta:
        model=Estudiante
        fields={
            'Cedula','Nombre','Apellido','Edad','Telefono','email','direccion','ocupaciones'
        }

