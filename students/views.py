# accounts/views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .serializers import UsuarioPerfilSerializer 

class EstudiantePerfilAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        user = request.user

        if not user.estudiante:
            return Response(
                {"detail": "No se encontró un perfil de estudiante asociado a este usuario."},
                status=status.HTTP_404_NOT_FOUND
            )
            
        serializer = UsuarioPerfilSerializer(user)
        
        return Response(serializer.data, status=status.HTTP_200_OK)
    


class EstudiantePerfilAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, format=None):
        user = request.user

        if not hasattr(user, 'estudiante') or not user.estudiante:
            return Response(
                {"detail": "No se encontró un perfil de estudiante asociado a este usuario."},
                status=status.HTTP_404_NOT_FOUND
            )
            
        serializer = UsuarioPerfilSerializer(user)
        
        return Response(serializer.data, status=status.HTTP_200_OK)

    def patch(self, request, format=None):
        user_instance = request.user
        
        if not hasattr(user_instance, 'estudiante') or not user_instance.estudiante:
             return Response(
                {"detail": "No se encontró un perfil de estudiante para actualizar."},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = UsuarioPerfilSerializer(
            user_instance, 
            data=request.data, 
            partial=True
        )

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)