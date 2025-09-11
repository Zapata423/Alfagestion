from django.db import models
from teachers.models import Docente
from accounts.models import Usuario
from model_utils.models import TimeStampedModel



class Validacion(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pendiente'),
        ('approved', 'Aprobada'),
        ('rejected', 'Rechazada'),
    ]
    actividad = models.ForeignKey('evidence.Actividad', on_delete=models.CASCADE, related_name="validaciones")
    docente = models.ForeignKey(Docente, on_delete=models.CASCADE, related_name="validaciones")
    comentarios = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    fecha_validacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.actividad} → {self.get_status_display()}"
    