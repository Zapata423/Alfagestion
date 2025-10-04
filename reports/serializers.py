from rest_framework import serializers
from evidence.models import Actividad
from reports.models import Validacion  # ajusta según tu estructura


class ActividadConEstadoSerializer(serializers.ModelSerializer):
    estado = serializers.SerializerMethodField()

    class Meta:
        model = Actividad
        fields = ["id", "titulo", "horas", "fecha_subida", "estado"]

    def get_estado(self, obj):
        # buscamos la última validación (si existe)
        validacion = obj.validaciones.order_by("-fecha_validacion").first()
        return validacion.get_status_display() if validacion else "Pendiente"
    

class ValidacionComentarioSerializer(serializers.ModelSerializer):
    actividad_id = serializers.IntegerField(source='actividad.id', read_only=True)

    class Meta:
        model = Validacion
        fields = ['actividad_id', 'comentarios']
