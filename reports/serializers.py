from rest_framework import serializers
from evidence.models import Actividad # ajusta según tu estructura
from .models import Validacion


class ActividadConEstadoSerializer(serializers.ModelSerializer):
    estado = serializers.SerializerMethodField()

    class Meta:
        model = Actividad
        fields = ["id", "titulo", "horas", "fecha_subida", "estado"]

    def get_estado(self, obj):
        # buscamos la última validación (si existe)
        validacion = obj.validaciones.order_by("-fecha_validacion").first()
        return validacion.get_status_display() if validacion else "Pendiente"