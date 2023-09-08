from django.urls import path
from .views import *

urlpatterns = [
    path("agrega_curso/<nombre>/<camada>", curso),
    path("lista_cursos/", listar_cursos),
    path("", inicio),
    path("cursos/",curso),
    path("profesores/", profesores),
    path("estudiantes/", estudiantes),
    path("entregables/", entregables),
    
    
]
