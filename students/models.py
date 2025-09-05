from django.db import models
from django.utils import timezone
from accounts.models import User
from django.db.models import Sum
from model_utils.models import TimeStampedModel


class Student(TimeStampedModel):
    user = models.OneToOneField('accounts.User', on_delete=models.CASCADE, related_name='student_profile', verbose_name="Usuario", null=True, blank=True)
    telefono = models.CharField(max_length=15, blank=True, null=True, verbose_name="Teléfono")
    fecha_nacimiento = models.DateField(verbose_name="Fecha de nacimiento")
    
    class Meta:
        verbose_name = "Estudiante"
        verbose_name_plural = "Estudiantes"
        ordering = ['user__last_name', 'user__first_name']
    
    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} - {self.user.grade}"
    
    @property
    def full_name(self):
        return f"{self.user.first_name} {self.user.last_name}"
    
    @property
    def first_name(self):
        return self.user.first_name
    
    @property
    def last_name(self):
        return self.user.last_name
    
    @property
    def email(self):
        return self.user.email
    
    @property
    def grade(self):
        return self.user.grade
    
    @property
    def date_joined(self):
        return self.user.date_joined

class HoursControl(TimeStampedModel):
    student = models.OneToOneField("Student", on_delete=models.CASCADE, related_name="control_horas")
    hours_required = models.IntegerField(default=80)  # Ejemplo: 80 horas de servicio social

    @property
    def hours_accumulated(self):
        """
        Calcula la suma de horas de todas las evidencias aprobadas del estudiante.
        """
        from evidence.models import Evidence
        
        total = Evidence.objects.filter(
            student=self.student,
            reports__state="aprobada"
        ).aggregate(suma=Sum("activity__hours"))["suma"]

        return total or 0  # si no hay horas aprobadas, devuelve 0

    def __str__(self):
        return f"{self.student} - {self.hours_accumulated}/{self.hours_required}"