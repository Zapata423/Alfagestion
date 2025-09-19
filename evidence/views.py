from django.shortcuts import render
from rest_framework.generics import RetrieveAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import Actividad
from .serializers import ActividadSerializer

class UploadActividadAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = ActividadSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            # asignar automáticamente el estudiante (usuario autenticado)
            actividad = serializer.save()
            return Response({
                "success": True,
                "message": "Actividad creada exitosamente",
                "id": actividad.id,
                "titulo": actividad.titulo,
                "institucion": {
                    "id": actividad.institucion.id,
                    "nombre": actividad.institucion.nombre
                },
                "encargado": {
                    "id": actividad.encargado.id if actividad.encargado else None,
                    "nombre": actividad.encargado.nombre if actividad.encargado else None
                },
                "creador": request.user.email,
                "fecha_subida": actividad.fecha_subida
            }, status=status.HTTP_201_CREATED)
        return Response({
            "success": False,
            "errors": serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)


