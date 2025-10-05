from django.db import models
from accounts.models import Usuario
from django.db.models import Sum

class Estudiante(models.Model):
    nombres = models.CharField(max_length=30, blank=True, null=True)
    apellidos = models.CharField(max_length=30, blank=True, null=True)
    telefono = models.CharField(max_length=15, blank=True, null=True, verbose_name="Teléfono")
    fecha_nacimiento = models.DateField(verbose_name="Fecha de nacimiento", blank=True, null=True)

    def __str__(self):
        return f"{self.nombres} {self.apellidos}"

class ControlHoras(models.Model):
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE, related_name="control_horas")
    horas_requeridas = models.IntegerField(default=80)  
    ultima_actualizacion = models.DateTimeField(auto_now=True)


    def horas_aprobadas(self):
        from evidence.models import Actividad
        return (
            Actividad.objects.filter(
                estudiante=self,
                validaciones__aprobada=True
            ).aggregate(suma=Sum("horas"))["suma"] or 0
        )

    def horas_subidas(self): 
        from evidence.models import Actividad 
        return ( 
            Actividad.objects.filter(
                estudiante=self.estudiante 
            ).aggregate(suma=Sum("horas"))["suma"] or 0 )


    def __str__(self): 
        return f"{self.estudiante} - {self.horas_aprobadas()} aprobadas / {self.horas_subidas()} subidas"


