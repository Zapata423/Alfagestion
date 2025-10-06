from rest_framework import serializers
from accounts.models import Usuario
from .models import Docente
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
    validacion_id = serializers.SerializerMethodField() 

    class Meta:
        model = Actividad
        fields = ["id", "titulo", "horas", "fecha_subida", "estado", "tiene_validacion", "validacion_id"]

    def get_estado(self, obj):
        validacion = obj.validaciones.first()
        return validacion.get_status_display() if validacion else "Pendiente"
    
    def get_tiene_validacion(self, obj):
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


class DocenteUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Docente
        fields = [
            'nombre',
            'apellido',
            'telefono',
            'fecha_nacimiento',
            'foto',
        ]


class UsuarioPerfilDocenteSerializer(serializers.ModelSerializer):
    docente = DocenteUpdateSerializer()

    class Meta:
        model = Usuario
        fields = [
            'docente', 
            'email',
            'cargo',    
        ]
        read_only_fields = ['email']

    def update(self, instance, validated_data):
        docente_data = validated_data.pop('docente', {})

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        if hasattr(instance, 'docente') and instance.docente:
            docente_instance = instance.docente

            for attr, value in docente_data.items():
                setattr(docente_instance, attr, value)

            docente_instance.save()

        return instance