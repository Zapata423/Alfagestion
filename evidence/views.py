from django.shortcuts import render
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
                "fecha_subida": actividad.fecha_subida,
                "archivo_url": request.build_absolute_uri(actividad.archivo.url) if actividad.archivo else None
            }, status=status.HTTP_201_CREATED)
        return Response({
            "success": False,
            "errors": serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

class DeleteActividadView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, pk):
        try:
            actividad = Actividad.objects.get(pk=pk, creador=request.user)
            actividad.delete()
            return Response({"detail": "Actividad eliminada correctamente."}, status=status.HTTP_204_NO_CONTENT)
        except Actividad.DoesNotExist:
            return Response({"detail": "Actividad no encontrada o no tienes permisos."}, status=status.HTTP_404_NOT_FOUND)

class MisActividadesView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        actividades = Actividad.objects.filter(creador=request.user)
        serializer = ActividadSerializer(
            actividades, many=True, context={"request": request}
        )
        return Response(serializer.data)