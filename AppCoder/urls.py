from django.urls import path
from .views import *

urlpatterns = [
    path("agrega_curso/<nombre>/<camada>", curso),
    path("lista_cursos/", listar_cursos, name="ListaCursos"),
    path("", inicio, name="Inicio"),
    path("cursos/",curso, name="Cursos"),
    path("profesores/", profesores, name="Profesores"),
    path("estudiantes/", estudiantes, name="Estudiantes"),
    path("entregables/", entregables, name="Entregable"),
    path("curso-formulario/", cursoFormulario, name="CursoFormulario"),
    path("busqueda-camada/", busquedaCamada, name="BusquedaCamada"),
    path("buscar/", buscar, name="Buscar"),
    
]
