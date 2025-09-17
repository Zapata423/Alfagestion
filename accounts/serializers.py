from rest_framework import serializers
from django.contrib.auth import authenticate
from accounts.models import Usuario  # Ajusta a tu modelo real
from rest_framework_simplejwt.tokens import RefreshToken


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
        # Crear tokens JWT
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
        # Crear tokens JWT
        refresh = RefreshToken.for_user(user)
        data["access"] = str(refresh.access_token)
        data["refresh"] = str(refresh)
        return data