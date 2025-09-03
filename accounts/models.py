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
    first_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=30, blank=True, null=True)
    role = models.ForeignKey(Role, on_delete=models.PROTECT, related_name="users")

    # Campos específicos por rol
    position = models.CharField(max_length=100, blank=True, null=True, help_text="Position of the teacher (e.g: Professor, Coordinator, Director)")
    grade = models.CharField(max_length=50, blank=True, null=True, help_text="Student grade (e.g: 1st, 2nd, 3rd)")

    # Relación con estudiante/docente (se definen en otras apps)
    estudiante_id = models.PositiveIntegerField(blank=True, null=True)
    docente_id = models.PositiveIntegerField(blank=True, null=True)
    # Datos adicionales
    date_joined = models.DateTimeField(default=timezone.now)

    def __str__(self):
        name = f"{self.first_name} {self.last_name}".strip() if self.first_name or self.last_name else self.username
        
        # Mostrar información específica según el rol
        if self.role and self.role.name:
            role_name = self.role.name.lower()
            if role_name == 'docente' and self.position:
                return f"{name} - {self.role.name} ({self.position})"
            elif role_name == 'estudiante' and self.grade:
                return f"{name} - {self.role.name} ({self.grade})"
            else:
                return f"{name} - {self.role.name}"
        
        return name


