from django.db import models
from institutions.models import Institucion, Encargado

# actividades(evidencia) calendario

class Actividad(models.Model):
    creador = models.ForeignKey('accounts.Usuario', on_delete=models.CASCADE, related_name='actividades_creadas', null=True, blank=True)
    institucion = models.ForeignKey(Institucion, on_delete=models.CASCADE, related_name="actividades")
    encargado = models.ForeignKey(Encargado, on_delete=models.CASCADE, related_name="actividades")

    titulo = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True, null=True)
    archivo = models.FileField(upload_to="evidencias/")
    horas = models.PositiveIntegerField(default=0)

    fecha_subida = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.titulo} - {self.creador}"

