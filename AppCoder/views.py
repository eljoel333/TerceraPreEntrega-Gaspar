from django.shortcuts import render
from .models import Curso
from django.http import HttpResponse

# Create your views here.

def crear_curso(request):
    nombre_curso = "programacion basica"
    comision_curso = 23456

    print('creando curso')
    curso = Curso(nombre = nombre_curso, comision = comision_curso)
    curso.save()
    respuesta = f"Curso creado: {curso.nombre} - {curso.comision}"

    return HttpResponse(respuesta)

def listar_cursos(request):
    cursos=Curso.objects.all()
    respuesta=""
    for curso in cursos:
        respuesta += f"{curso.nombre} - {curso.comision}<br>"
    return HttpResponse(respuesta)


def inicio(request):
    return render(request, "AppCoder/inicio.html")

def profesores(request):
        return render(request, "AppCoder/profesores.html")


def estudiantes(request):
        return render(request, "AppCoder/estudiantes.html")


def cursos(request):
        return render(request, "AppCoder/cursos.html")


def entregables(request):
        return render(request, "AppCoder/entregables.html")
