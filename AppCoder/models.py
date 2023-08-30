from django.db import models

# Create your models here.
class Curso(models.Model):
    nombre = models.CharField(max_length=50)
    comision = models.IntegerField()
    def __str__(self) -> str:
        return f"{self.nombre}-{self.comision}"

class Estudiante(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()
    def __str__(self) -> str:
        return f"{self.nombre}-{self.apellido}-{self.email}"

class Profesor(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()
    profesion = models.CharField(max_length=50)
    def __str__(self) -> str:
        return f"{self.nombre}-{self.profesion}"

class Entregable(models.Model):
    nombre = models.CharField(max_length=50)
    fecha_entrega = models.DateField()
    entregado= models.BooleanField()


class Clientes(models.Model):
    nombreCliente = models.CharField(max_length=50)
    apellidosCliente = models.CharField(max_length=50)
    correoCliente = models.CharField(max_length=50)
    adeuda=  models.BooleanField()

class Articulos(models.Model):
    claveArticulo = models.CharField(max_length=50)
    descripcionArticulo = models.CharField(max_length=50)
    numExistencia = models.IntegerField()

    