from django.db import models



class Rol(models.Model):
    nombre = models.CharField(max_length=50, blank=True, null=True, unique=True)  # estudiante, docente, admin
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre


class Usuario(models.Model):
    usuario = models.CharField(max_length=50, unique=True, blank=False, null=False)
    password = models.CharField(max_length=50, blank=False, null=False)
    email = models.EmailField(unique=True, null=True, blank=True)
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE, related_name="usuarios")
    estudiante = models.OneToOneField("students.Estudiante", on_delete=models.SET_NULL, null=True, blank=True)
    docente = models.OneToOneField("teachers.Docente", on_delete=models.SET_NULL, null=True, blank=True)
    creado_en = models.DateTimeField(auto_now_add=True)

    cargo = models.CharField(max_length=100, blank=True, null=True, help_text="Position of the teacher (e.g: Professor, Coordinator, Director)")
    grado = models.CharField(max_length=50, blank=True, null=True, help_text="Student grade (e.g: 1st, 2nd, 3rd)")




    def __str__(self):
        # Usamos usuario o email porque no existen nombre y apellido en este modelo
        nombreCompleto = self.usuario or (self.email if self.email else "Usuario sin nombre")

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


