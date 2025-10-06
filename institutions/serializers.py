from rest_framework import serializers
from .models import Institucion, Encargado


class InstitucionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Institucion
        fields = ['id', 'nombre', 'poblacion_intervenida', 'direccion', 'barrio', 'ciudad', 'telefono', 'email',]
        extra_kwargs = {
            'creador': {'write_only': True}
        }

    def create(self, validated_data):
        validated_data['creador'] = self.context['request'].user
        return super().create(validated_data)


class EncargadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Encargado
        fields = ['id', 'nombre', 'apellido', 'correo', 'telefono', 'cargo', 'observaciones',]
        extra_kwargs = {
            'creador': {'write_only': True}  
        }

    def create(self, validated_data):
        validated_data['creador'] = self.context['request'].user
        return super().create(validated_data)