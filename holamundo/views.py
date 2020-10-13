from django.shortcuts import render
from django.http import HttpResponse
from holamundo.models import Carrera, Paralelo, Estudiante
from rest_framework import viewsets
from holamundo.serializers import CarreraSerializer,ParaleloSerializer,EstudianteSerializer

#Insertar vistas
class CarreraViewSet(viewsets.ModelViewSet):
    queryset=Carrera.objects.all().order_by('nombreCarrera')
    serializer_class=CarreraSerializer

class ParaleloViewSet(viewsets.ModelViewSet):
    queryset=Paralelo.objects.all().order_by('ciclo')
    serializer_class=ParaleloSerializer

class EstudianteViewSet(viewsets.ModelViewSet):
    queryset=Estudiante.objects.all().order_by('Cedula')
    serializer_class=EstudianteSerializer

def index(request):
    return HttpResponse("Hola mundo, Es la primera Aplicacion soy Jonathan Sarmiento")
