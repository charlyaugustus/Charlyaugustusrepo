from django.contrib import admin
from .models import Curso, Profesores, Estudiante, Entregables

# Register your models here.
admin.site.register(Curso)
admin.site.register(Profesores)
admin.site.register(Estudiante)
admin.site.register(Entregables)