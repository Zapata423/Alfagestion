from rest_framework import serializers
from evidence.models import Actividad
from institutions.models import Institucion, Encargado

class ActividadSerializer(serializers.ModelSerializer):
    institucion = serializers.PrimaryKeyRelatedField(queryset=Institucion.objects.all())
    encargado = serializers.PrimaryKeyRelatedField(queryset=Encargado.objects.all(), required=False)

    class Meta:
        model = Actividad
        fields = ['titulo', 'descripcion', 'archivo', 'horas', 'institucion', 'encargado']
        extra_kwargs = {
            'archivo': {'required': True},
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        request = self.context.get('request')
        if request and request.user.is_authenticated and hasattr(request.user, 'estudiante') and request.user.estudiante:
            self.fields['institucion'].queryset = Institucion.objects.filter(creador=request.user)
            self.fields['encargado'].queryset = Encargado.objects.filter(institucion__creador=request.user)

class InstitucionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Institucion
        fields = ['id', 'nombre', 'poblacion_intervenida', 'direccion', 'telefono', 'email', 'telefono_contacto']

class EncargadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Encargado
        fields = ['id', 'institucion', 'nombre', 'apellido', 'correo', 'telefono', 'cargo']
