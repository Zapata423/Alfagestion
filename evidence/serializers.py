
from rest_framework import serializers
from .models import Actividad
from institutions.models import Institucion, Encargado

class ActividadSerializer(serializers.ModelSerializer):
    institucion_nombre = serializers.CharField(source="institucion.nombre", read_only=True)
    encargado_nombre = serializers.CharField(source="encargado.nombre", read_only=True)

    class Meta:
        model = Actividad
        fields = [
            "id", "titulo", "descripcion", "archivo", "horas",
            "fecha_subida", "creador",
            "institucion", "institucion_nombre",
            "encargado", "encargado_nombre"
        ]
        extra_kwargs = {
            'creador': {'write_only': True}  # no lo envía el cliente, lo asignamos automático
        }

    def create(self, validated_data):
        validated_data['creador'] = self.context['request'].user
        return super().create(validated_data)
