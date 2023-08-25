from django.http import HttpResponse

def saludar(request):
    return HttpResponse("holaaa")

def segundaVista(request):
    return HttpResponse("<h1>Hola segunda vista</h1>")

def saludo_con_nombre(reques, nombre):
    return HttpResponse(f"<h1>hola: {nombre}</h1>")