
from rest_framework import serializers
from students.models import Estudiante
from accounts.models import Usuario


class EstudianteUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estudiante
        fields = [
            'nombres', 
            'apellidos', 
            'telefono', 
            'fecha_nacimiento',
            'foto',
        ]
        

class UsuarioPerfilSerializer(serializers.ModelSerializer):
    estudiante = EstudianteUpdateSerializer() 
    class Meta:
        model = Usuario
        fields = [
            'estudiante', 
            'email',       
            'grado',       
            'grupo',        
        ]
        read_only_fields = ['email', 'grado', 'grupo']
        
    def update(self, instance, validated_data):
        estudiante_data = validated_data.pop('estudiante', {})
        
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        if hasattr(instance, 'estudiante') and instance.estudiante:
            estudiante_instance = instance.estudiante 
            
            for attr, value in estudiante_data.items():
                setattr(estudiante_instance, attr, value)
                
            estudiante_instance.save()

        return instance