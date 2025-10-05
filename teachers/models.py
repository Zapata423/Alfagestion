from django.db import models

class Docente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    telefono = models.CharField(max_length=50, blank=True, null=True)
    fecha_nacimiento = models.DateField(verbose_name="Fecha de nacimiento", blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


