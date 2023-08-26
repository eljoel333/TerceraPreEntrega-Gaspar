from django.http import HttpResponse

from django.template import Template, Context, loader



def saludar(request):
    return HttpResponse("holaaa")

def segundaVista(request):
    return HttpResponse("<h1>Hola segunda vista</h1>")

def saludo_con_nombre(reques, nombre):
    return HttpResponse(f"<h1>hola: {nombre}</h1>")

def plantillaHTML(request):

    diccionario = {"Nombre":"Joel", "Apellido":"gaspar", "Edad":"38", "listanotas":[1,2,3,4,5,6,7,8,9]}

   
    template = loader.get_template("template1.html")
   
    documento = template.render(diccionario)
    return HttpResponse(documento)
