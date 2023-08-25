from django.http import HttpResponse

from django.template import Template, Context

def saludar(request):
    return HttpResponse("holaaa")

def segundaVista(request):
    return HttpResponse("<h1>Hola segunda vista</h1>")

def saludo_con_nombre(reques, nombre):
    return HttpResponse(f"<h1>hola: {nombre}</h1>")

def plantillaHTML(request):

    diccionario = {"Nombre":"Joel", "Apellido":"gaspar", "Edad":"38"}

    archivo = open(r"C:\Users\JoelGH\Documents\Cursos\CoderHouse\Python\Clase17\Entrega3\entrega3-env\proyecto3\proyecto3\plnatillas\template1.html")
    contenido = archivo.read()
    archivo.close()
    template = Template(contenido)
    contexto = Context(diccionario)
    documento = template.render(contexto)
    return HttpResponse(documento)
