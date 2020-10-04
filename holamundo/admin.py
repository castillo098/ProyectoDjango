from django.contrib import admin
from .models import Carrera
from .models import Paralelo
from .models import Estudiante

# Register your models here.
admin .site.register(Carrera)
admin .site.register(Paralelo)
admin .site.register(Estudiante)

