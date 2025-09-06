from django.db import models
from teachers.models import Docente
from accounts.models import Usuario
from model_utils.models import TimeStampedModel



class Validacion(models.Model):
    actividad = models.ForeignKey('evidence.Actividad', on_delete=models.CASCADE, related_name="validaciones")
    docente = models.ForeignKey(Docente, on_delete=models.CASCADE, related_name="validaciones")
    comentarios = models.TextField()
    aprobada = models.BooleanField(default=False)
    fecha_validacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        estado = "Aprobada" if self.aprobada else "Rechazada"
        return f"{self.actividad} → {estado}"
    