from rest_framework import serializers
from django.contrib.auth import authenticate
from accounts.models import Usuario  
from rest_framework_simplejwt.tokens import RefreshToken
from django.db import transaction
from students.models import Estudiante
from teachers.models import Docente
from .models import Rol


class LoginTeacherSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        email = data.get("email")
        password = data.get("password")

        user = authenticate(email=email, password=password)

        if not user:
            raise serializers.ValidationError("Credenciales inválidas.")

        if user.rol.nombre.lower() != "docente":
            raise serializers.ValidationError("Solo los Docentes pueden iniciar sesión aquí.")

        data["user"] = user

        refresh = RefreshToken.for_user(user)
        data["access"] = str(refresh.access_token)
        data["refresh"] = str(refresh)
        return data
    

class LoginStudentsSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        email = data.get("email")
        password = data.get("password")

        user = authenticate(email=email, password=password)

        if not user:
            raise serializers.ValidationError("Credenciales inválidas.")

        if user.rol.nombre.lower() != "estudiante":
            raise serializers.ValidationError("Solo los Estudiantes pueden iniciar sesión aquí.")

        data["user"] = user

        refresh = RefreshToken.for_user(user)
        data["access"] = str(refresh.access_token)
        data["refresh"] = str(refresh)
        return data
    

class LoginAdminSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        email = data.get("email")
        password = data.get("password")

        user = authenticate(email=email, password=password)

        if not user:
            raise serializers.ValidationError("Credenciales inválidas. Verifique su correo y contraseña.")
        
        if not user.is_superuser:
            raise serializers.ValidationError("Solo los Administradores principales pueden iniciar sesión en este portal.")
        
        data["user"] = user

        refresh = RefreshToken.for_user(user)
        data["access"] = str(refresh.access_token)
        data["refresh"] = str(refresh)
        
        return data


class EstudianteRegistroCompletoSerializer(serializers.ModelSerializer):
    password_confirm = serializers.CharField(write_only=True)
    nombres = serializers.CharField(max_length=30)
    apellidos = serializers.CharField(max_length=30)
    telefono = serializers.CharField(max_length=15,write_only=True, required=False, allow_blank=True) 
    fecha_nacimiento = serializers.DateField()
    rol_nombre = serializers.CharField(write_only=True, default='Estudiante')
    
    class Meta:
        model = Usuario
        fields = (
            'email', 'password', 'password_confirm', 
            'grado', 'grupo', 
            'nombres', 'apellidos', 'telefono', 'fecha_nacimiento',
            'rol_nombre'
        )
        extra_kwargs = {
            'password': {'write_only': True},
            'grado': {'required': True},    
            'grupo': {'required': True},
        }

    def validate(self, data):
        if data['password'] != data['password_confirm']:
            raise serializers.ValidationError({"password_confirm": "Las contraseñas no coinciden."})
        
        if data.get('rol_nombre', '').lower() != 'estudiante':
             raise serializers.ValidationError({"rol_nombre": "Solo se permite el registro con el rol 'Estudiante' en este endpoint."})
        
        return data

    @transaction.atomic
    def create(self, validated_data):
        """Crea el Estudiante, luego el Usuario, y establece el vínculo OneToOne."""

        email = validated_data['email']
        password = validated_data['password']
        grado = validated_data['grado']
        grupo = validated_data['grupo']
        
        datos_estudiante = {
            'nombres': validated_data['nombres'],
            'apellidos': validated_data['apellidos'],
            'telefono': validated_data['telefono'],
            'fecha_nacimiento': validated_data['fecha_nacimiento'],
        }
        
        rol_nombre = validated_data.pop('rol_nombre').lower()
        validated_data.pop('password_confirm') 
        
        
        nuevo_estudiante = Estudiante.objects.create(**datos_estudiante)
        
        try:
            rol_obj = Rol.objects.get(nombre__iexact=rol_nombre)
        except Rol.DoesNotExist:
            raise serializers.ValidationError({"rol_nombre": f"El rol '{rol_nombre}' no existe."})

        user = Usuario.objects.create_user(
            email=email,
            password=password
        )
        
        user.rol = rol_obj
        user.estudiante = nuevo_estudiante 
        user.grado = grado
        user.grupo = grupo
        
        user.save()
        return user
    

class DocenteRegistroCompletoSerializer(serializers.ModelSerializer):
    password_confirm = serializers.CharField(write_only=True)
    nombre = serializers.CharField(max_length=30)
    apellido = serializers.CharField(max_length=30)
    telefono = serializers.CharField(max_length=15,write_only=True, required=False, allow_blank=True) 
    fecha_nacimiento = serializers.DateField()
    rol_nombre = serializers.CharField(write_only=True, default='Docente')
    
    class Meta:
        model = Usuario
        fields = (
            'email', 'password', 'password_confirm', 'cargo', 
            'nombre', 'apellido', 'telefono', 'fecha_nacimiento',
            'rol_nombre'
        )
        extra_kwargs = {
            'password': {'write_only': True},
            'cargo': {'required': True, 'allow_blank': False}, 
        }

    def validate(self, data):
        if data['password'] != data['password_confirm']:
            raise serializers.ValidationError({"password_confirm": "Las contraseñas no coinciden."})
        
        if data.get('rol_nombre', '').lower() != 'docente':
             raise serializers.ValidationError({"rol_nombre": "Solo se permite el registro con el rol 'Docente' en este endpoint."})
        
        if not data.get('cargo', '').strip():
             raise serializers.ValidationError({"cargo": "El cargo no puede estar vacío."})
        
        return data

# decorador(funcion que envuelve otra funcion), se cguaarda completo, si hay algo incorrecto revierte
    @transaction.atomic
    def create(self, validated_data):

        email = validated_data['email']
        password = validated_data['password']
        cargo = validated_data['cargo'] 

        datos_docente = {
            'nombre': validated_data.pop('nombre'),
            'apellido': validated_data.pop('apellido'),
            'telefono': validated_data.pop('telefono'),
            'fecha_nacimiento': validated_data.pop('fecha_nacimiento'),
        }
        
        rol_nombre = validated_data.pop('rol_nombre').lower()
        validated_data.pop('password_confirm')   # pop es que lo elimina
        validated_data.pop('cargo') 

        nuevo_docente = Docente.objects.create(**datos_docente)
        
        try:
            rol_obj = Rol.objects.get(nombre__iexact=rol_nombre)
        except Rol.DoesNotExist:
            raise serializers.ValidationError({"rol_nombre": f"El rol '{rol_nombre}' no existe."})

        user = Usuario.objects.create_user(
            email=email,
            password=password
        )
        
        user.rol = rol_obj
        user.docente = nuevo_docente 
        user.cargo = cargo  

        user.save()
        return user