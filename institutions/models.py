from django.db import models
from django.utils import timezone

class Institucion(models.Model):
    nombre = models.CharField(max_length=200)
    poblacion_intervenida = models.CharField(max_length=100, blank=True, null=True)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    nombre_contacto = models.CharField(max_length=100, blank=True, null=True)
    telefono_contacto = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.nombre
    
class Encargado(models.Model):
    institucion = models.ForeignKey(Institucion, on_delete=models.CASCADE, related_name="encargados")
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    correo = models.EmailField()
    telefono = models.CharField(max_length=50, blank=True, null=True)
    cargo = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido} ({self.institucion.nombre})"


