from rest_framework import serializers, pagination
from accounts.models import Usuario
from students.models import Estudiante
from evidence.models import Actividad
from institutions.models import Institucion, Encargado
from django.contrib.auth.models import User


class GradoSerializer(serializers.Serializer):
    grado = serializers.CharField()


class GrupoSerializer(serializers.Serializer):
    grupo = serializers.CharField()


class EstudianteSerializer(serializers.ModelSerializer):
    nombre_completo = serializers.SerializerMethodField()

    class Meta:
        model = Usuario
        fields = ('nombre_completo', 'grado', 'grupo')

    def get_nombre_completo(self, obj):
        if obj.estudiante:
            return f"{obj.estudiante.nombres} {obj.estudiante.apellidos}"
        return obj.email


class InstitucionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Institucion
        fields = '__all__'


class EncargadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Encargado
        fields = '__all__'


class ActividadSerializer(serializers.ModelSerializer):
    institucion = InstitucionSerializer(read_only=True)
    encargado = EncargadoSerializer(read_only=True, allow_null=True)

    class Meta:
        model = Actividad
        fields = ('titulo', 'descripcion', 'archivo', 'horas', 'institucion', 'encargado')




