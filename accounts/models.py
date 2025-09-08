from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import UserManager



class Rol(models.Model):
    nombre = models.CharField(max_length=50, blank=True, null=True, unique=True)  # estudiante, docente, admin
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre


class Usuario(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE, related_name="usuarios", blank=True, null=True)
    estudiante = models.OneToOneField("students.Estudiante", on_delete=models.SET_NULL, null=True, blank=True)
    docente = models.OneToOneField("teachers.Docente", on_delete=models.SET_NULL, null=True, blank=True)
    creado_en = models.DateTimeField(auto_now_add=True, blank=True)

    cargo = models.CharField(max_length=100, blank=True, null=True, help_text="( Professor, Coordinator, Director)")
    grado = models.CharField(max_length=50, blank=True, null=True, help_text="Si es estudiante")

    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'

    objects = UserManager()




    def __str__(self):
        # Usamos el email como identificador principal
        nombreCompleto = self.email or "Usuario sin email"

        # Mostrar información específica según el rol
        if self.rol and hasattr(self.rol, "nombre"):
            nombre_rol = self.rol.nombre.lower()
            if nombre_rol == "docente" and self.cargo:
                return f"{nombreCompleto} - {self.rol.nombre} ({self.cargo})"
            elif nombre_rol == "estudiante" and self.grado:
                return f"{nombreCompleto} - {self.rol.nombre} ({self.grado})"
            else:
                return f"{nombreCompleto} - {self.rol.nombre}"

        return nombreCompleto


