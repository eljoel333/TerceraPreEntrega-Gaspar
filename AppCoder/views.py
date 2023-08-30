from django.shortcuts import render
from .models import *
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
        if request.method == "POST":
              pass
        else:
              
            profesores = Profesor.objects.all()
        return render(request, "AppCoder/profesores.html", {"profesores": profesores})


def estudiantes(request):
        est = Estudiante.objects.all()
        return render(request, "AppCoder/estudiantes.html", {"misestudiantes":est})

def cursoFormulario(request):
        if  request.method == 'POST':
            nombre = request.POST["nombre"]
            comision = request.POST["comision"]
            curso = Curso(nombre=nombre, comision=comision)
            curso.save()
            return render(request, "AppCoder/cursoFormulario.html", {"mensaje": "Curso creado"})
        else:
            return render(request, "AppCoder/cursoFormulario.html")



def cursos(request):
        cursos = Curso.objects.all()
        return render(request, "AppCoder/cursos.html", {"cursos":cursos})


def entregables(request):
        return render(request, "AppCoder/entregables.html")


def estudianteFormulario(request):
        if  request.method == 'POST':
            nombre = request.POST["nombre"]
            print(nombre)
            apellido = request.POST["apellido"]
            print(apellido)

            email = request.POST["email"]
            print(email)

            est = Estudiante(nombre=nombre, apellido=apellido, email=email)
            est.save()
            return render(request, "AppCoder/estudianteFormulario.html", {"mensaje": "El estudiante fue dado de alta"})
        else:
            return render(request, "AppCoder/estudianteFormulario.html")



def clienteFormulario(request):
        if  request.method == 'POST':
            nombre = request.POST["nombre"]
            print(nombre)
            apellidos = request.POST["apellidos"]
            print(apellidos)

            correo = request.POST["correo"]
            print(correo)

            adeuda = request.POST["adeuda"]
            print(adeuda)

           
            client = Clientes(nombreCliente = nombre, apellidosCliente = apellidos, correoCliente = correo, adeuda= adeuda)
            client.save();

            return render(request, "AppCoder/clienteFormulario.html", {"mensaje": "El cliente fue dado de alta"})

        else:
            est = Clientes.objects.all()
            return render(request, "AppCoder/clienteFormulario.html")
        
def clientes(request):
        est = Clientes.objects.all()
        return render(request, "AppCoder/clientes.html", {"misclientes":est})