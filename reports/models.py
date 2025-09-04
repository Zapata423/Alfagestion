from django.db import models
from evidence.models import Evidence
from accounts.models import User


class Report(models.Model):
    ESTADOS = [
        ('pendiente', 'Pendiente'),
        ('aprobada', 'Aprobada'),
        ('rechazada', 'Rechazada'),
    ]
    report = models.ForeignKey(Evidence, on_delete=models.CASCADE, related_name="reports")
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reports")  # docentes como usuarios
    state = models.CharField(max_length=20, choices=ESTADOS, default="pendiente")
    comments = models.TextField(blank=True, null=True)
    validation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.state} - {self.report}"