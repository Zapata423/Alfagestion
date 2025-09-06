from django.db import models
from institutions.models import Institucion, Encargado

# actividades(evidencia) calendario

class Actividad(models.Model):
    estudiante = models.ForeignKey('students.Estudiante', on_delete=models.CASCADE, related_name="actividades")
    institucion = models.ForeignKey(Institucion, on_delete=models.CASCADE, related_name="actividades")
    encargado = models.ForeignKey(Encargado, on_delete=models.SET_NULL, null=True, blank=True, related_name="actividades")

    titulo = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True, null=True)
    archivo = models.FileField(upload_to="evidencias/")
    horas = models.PositiveIntegerField(default=0)

    fecha_subida = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.titulo} - {self.estudiante}"

