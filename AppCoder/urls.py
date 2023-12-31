
from django.urls import path
from .views import *

urlpatterns = [

    path('crear_curso', crear_curso),
    path('listar_cursos', listar_cursos),
    path('', inicio),
    path('profesores/', profesores, name="profesores"),
    path('estudiantes/', estudiantes, name="estudiantes"),
    path('cursos/', cursos, name="cursos"),
    path('entregables/', entregables, name="entregables"),
    path('cursoFormulario/', cursoFormulario, name="cursoFormulario"),
    path('estudianteFormulario/', estudianteFormulario, name="estudianteFormulario"),
    path('clienteFormulario/', clienteFormulario, name="clienteFormulario"),
    path('clientes/', clientes, name="clientes"),
    path('articulosFormulario/', articulosFormulario, name="articulosFormulario"),
    path('articulos/', articulos, name="articulos"),

]
