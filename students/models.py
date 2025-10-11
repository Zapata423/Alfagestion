from django.db import models
from django.db.models import Sum


class Estudiante(models.Model):
    nombres = models.CharField(max_length=30, blank=True, null=True)
    apellidos = models.CharField(max_length=30, blank=True, null=True)
    telefono = models.CharField(max_length=15, blank=True, null=True, verbose_name="Teléfono")
    fecha_nacimiento = models.DateField(verbose_name="Fecha de nacimiento", blank=True, null=True)
    foto = models.ImageField(upload_to='perfiles/estudiantes/', null=True, blank=True, verbose_name="Foto de Perfil")

    def __str__(self):
        return f"{self.nombres} {self.apellidos}"
