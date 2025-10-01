from rest_framework import serializers
from accounts.models import Usuario
from evidence.models import Actividad
from institutions.models import Institucion, Encargado
from django.db.models import Sum
from reports.models import Validacion



class EstudianteConHorasSerializer(serializers.ModelSerializer):
    horas_subidas = serializers.SerializerMethodField()
    horas_verificadas = serializers.SerializerMethodField()
    ultima_carga = serializers.SerializerMethodField()
    nombre = serializers.SerializerMethodField()

    class Meta:
        model = Usuario
        fields = [
            "id", "nombre", "grado", "grupo",
            "horas_subidas", "horas_verificadas", "ultima_carga"
        ]

    def get_nombre(self, obj):
        return f"{obj.estudiante.nombres} {obj.estudiante.apellidos}" if obj.estudiante else obj.email

    def get_horas_subidas(self, obj):
        from evidence.models import Actividad
        return (
            Actividad.objects.filter(creador=obj)
            .aggregate(suma=Sum("horas"))["suma"] or 0
        )

    def get_horas_verificadas(self, obj):
        from evidence.models import Actividad
        return (
            Actividad.objects.filter(
                creador=obj,
                validaciones__status="approved"
            ).aggregate(suma=Sum("horas"))["suma"] or 0
        )

    def get_ultima_carga(self, obj):
        from evidence.models import Actividad
        ultima = (
            Actividad.objects.filter(creador=obj)
            .order_by("-fecha_subida")
            .first()
        )
        return ultima.fecha_subida if ultima else None
    

        
class ActividadesEstudianteSerializer(serializers.ModelSerializer):
    estado = serializers.SerializerMethodField()
    tiene_validacion = serializers.SerializerMethodField()
    validacion_id = serializers.SerializerMethodField()  # nuevo campo

    class Meta:
        model = Actividad
        fields = ["id", "titulo", "horas", "fecha_subida", "estado", "tiene_validacion", "validacion_id"]

    def get_estado(self, obj):
        # Tomamos la validación asociada (solo hay una)
        validacion = obj.validaciones.first()
        return validacion.get_status_display() if validacion else "Pendiente"
    
    def get_tiene_validacion(self, obj):
        # True si existe la validación
        return obj.validaciones.exists()
    
    def get_validacion_id(self, obj):
        validacion = obj.validaciones.first()
        return validacion.id if validacion else None

class EvidenciaActividadSerializer(serializers.ModelSerializer):
    institucion_nombre = serializers.CharField(source="institucion.nombre", read_only=True)
    encargado_nombre = serializers.CharField(source="encargado.nombre", read_only=True)
    archivo_url = serializers.SerializerMethodField()

    class Meta:
        model = Actividad
        fields = [
            "id", "titulo", "descripcion", "archivo", "archivo_url", "horas",
            "fecha_subida",
            "institucion", "institucion_nombre",
            "encargado", "encargado_nombre"
        ]

    def get_archivo_url(self, obj):
        request = self.context.get('request')
        if obj.archivo and hasattr(obj.archivo, "url"):
            return request.build_absolute_uri(obj.archivo.url)


class EvidenciaInstitucionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Institucion
        fields = ["id", "nombre", "poblacion_intervenida", "direccion", "barrio", "ciudad",
                  "telefono", "email",]

class EvidenciaEncargadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Encargado
        fields = ["id", "nombre", "apellido", "correo", "telefono", "cargo", "observaciones",]


class ValidacionSerializer(serializers.ModelSerializer):
    validacion_enviada = serializers.SerializerMethodField()
    class Meta:
        model = Validacion
        fields = ["id", "actividad", "comentarios", "status", "fecha_validacion", "validacion_enviada"]
        read_only_fields = ["id", "fecha_validacion", "docente", "actividad"]

    def get_validacion_enviada(self, obj):
        return obj.actividad.validaciones.exists()