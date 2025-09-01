from django.db import models
from django.utils import timezone



class Role(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True, unique=True)  # estudiante, docente, admin
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class User(models.Model):
    username = models.CharField(max_length=50, unique=True, blank=False, null=False)
    password = models.CharField(max_length=50, blank=False, null=False)
    email = models.EmailField(unique=True, null=True, blank=True)
    role = models.ForeignKey(Role, on_delete=models.PROTECT, related_name="users")
    # Relación con estudiante/docente (se definen en otras apps)
    estudiante_id = models.PositiveIntegerField(blank=True, null=True)
    docente_id = models.PositiveIntegerField(blank=True, null=True)

    # Datos adicionales
    date_joined = models.DateTimeField(default=timezone.now)
    last_login = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.username}"



# class InstitutionManager(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="institution_roles")
#     institution = models.ForeignKey("institutions.Institution", on_delete=models.CASCADE, related_name="managers")
#     role_in_institution = models.CharField(max_length=100, blank=True, null=True)  # ej: Coordinador, Tutor
#     assigned_at = models.DateField(auto_now_add=True)

#     def __str__(self):
#         return f"{self.user.username} - {self.role_in_institution} ({self.institution.name})"

