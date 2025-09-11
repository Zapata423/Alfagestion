from rest_framework import serializers, pagination
from accounts.models import Usuario
from students.models import Estudiante
from evidence.models import Actividad
from institutions.models import Institucion, Encargado
from reports.models import Validacion
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



class ValidacionSerializer(serializers.ModelSerializer):
    actividad = serializers.PrimaryKeyRelatedField(queryset=Actividad.objects.all())
    status = serializers.ChoiceField(choices=Validacion.STATUS_CHOICES, required=True)

    class Meta:
        model = Validacion
        fields = ['id', 'actividad', 'docente', 'comentarios', 'status', 'fecha_validacion']
        read_only_fields = ['docente', 'fecha_validacion']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        estudiante_id = self.context.get('estudiante_id')
        if estudiante_id:
            self.fields['actividad'].queryset = Actividad.objects.filter(estudiante_id=estudiante_id)
        else:
            self.fields['actividad'].queryset = Actividad.objects.none()
