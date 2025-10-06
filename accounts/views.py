from .models import Usuario
from rest_framework.response import Response
from rest_framework import status
from .serializers import LoginTeacherSerializer, LoginStudentsSerializer, LoginAdminSerializer, EstudianteRegistroCompletoSerializer, DocenteRegistroCompletoSerializer
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
        

class LoginUserStudentsAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = LoginStudentsSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data["user"]
            return Response({
                "success": True,
                "message": "Inicio de sesión exitoso",
                "user": {
                    "id": user.id,
                    "email": user.email,
                    "rol": user.rol.nombre,
                },
                "access": serializer.validated_data["access"],
                "refresh": serializer.validated_data["refresh"]
            }, status=status.HTTP_200_OK)
        return Response({
            "success": False,
            "errors": serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)
        

class LoginUserTeachersAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = LoginTeacherSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data["user"]
            return Response({
                "success": True,
                "message": "Inicio de sesión exitoso",
                "user": {
                    "id": user.id,
                    "email": user.email,
                    "rol": user.rol.nombre,
                },
                "access": serializer.validated_data["access"],
                "refresh": serializer.validated_data["refresh"]
            }, status=status.HTTP_200_OK)
        return Response({
            "success": False,
            "errors": serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)
    

class LoginUserAdminAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = LoginAdminSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data["user"]
            return Response({
                "success": True,
                "message": "Inicio de sesión exitoso",
                "user": {
                    "id": user.id,
                    "email": user.email,
                    "rol": user.rol,
                },
                "access": serializer.validated_data["access"],
                "refresh": serializer.validated_data["refresh"]
            }, status=status.HTTP_200_OK)
        return Response({
            "success": False,
            "errors": serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)
        

class LogoutAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            refresh_token = request.data.get("refresh")
            if not refresh_token:
                return Response({"success": False, "error": "Se requiere el refresh token"}, status=status.HTTP_400_BAD_REQUEST)

            token = RefreshToken(refresh_token)
            token.blacklist()  
            return Response({"success": True, "message": "Logout exitoso"}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"success": False, "error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


class EstudianteRegistroCompletoAPIView(APIView): 
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        serializer = EstudianteRegistroCompletoSerializer(data=request.data)

        if serializer.is_valid():
            try:
                user = serializer.save()
                response_data = {
                    "mensaje": "Registro de Estudiante y Cuenta completado exitosamente.",
                    "usuario_creado": user.email,
                    "nombres": user.estudiante.nombres,
                    "grado": user.grado,
                }
                return Response(response_data, status=status.HTTP_201_CREATED)

            except Exception as e:
                print(f"Error durante el guardado: {e}")
                return Response(
                    {"error": "Ocurrió un error interno al crear el registro."},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR
                )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


class DocenteRegistroCompletoAPIView(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        serializer = DocenteRegistroCompletoSerializer(data=request.data)

        if serializer.is_valid():
            try:
                user = serializer.save()
                
                response_data = {
                    "mensaje": "Registro de Docente y Cuenta completado exitosamente.",
                    "usuario_creado": user.email,
                    "nombre": user.docente.nombre, 
                    "cargo": user.cargo, 
                }
                return Response(response_data, status=status.HTTP_201_CREATED)

            except Exception as e:
                print(f"Error durante el guardado del Docente: {e}")
                return Response(
                    {"error": "Ocurrió un error interno al crear el registro del docente."},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR
                )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)