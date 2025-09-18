from django.shortcuts import render
from rest_framework.generics import RetrieveAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import Institucion, Encargado
from .serializers import InstitucionSerializer, EncargadoSerializer

# Create your views here.


class MisInstitucionesView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        instituciones = Institucion.objects.filter(creador=request.user)
        serializer = InstitucionSerializer(instituciones, many=True)
        return Response(serializer.data)

class MisEncargadosView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        encargados = Encargado.objects.filter(creador=request.user)
        serializer = EncargadoSerializer(encargados, many=True)
        return Response(serializer.data)


class UploadInstitucionAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = InstitucionSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            institucion = serializer.save()
            return Response({
                "success": True,
                "message": "Institucion creada exitosamente",
                "id": institucion.id
            }, status=status.HTTP_201_CREATED)

        return Response({
            "success": False,
            "errors": serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

class UploadEncargadoAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = EncargadoSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            encargado = serializer.save()
            return Response({
                "success": True,
                "message": "Encargado creado exitosamente",
                "id": encargado.id,
                "creador": encargado.creador.email
            }, status=status.HTTP_201_CREATED)
        return Response({
            "success": False,
            "errors": serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)
    

class DeleteEncargadoView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, pk):
        try:
            encargado = Encargado.objects.get(pk=pk, creador=request.user)
            encargado.delete()
            return Response({"detail": "Encargado eliminado correctamente."}, status=status.HTTP_204_NO_CONTENT)
        except Encargado.DoesNotExist:
            return Response({"detail": "Encargado no encontrado o no tienes permisos."}, status=status.HTTP_404_NOT_FOUND)
        
class DeleteInstitucionView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, pk):
        try:
            institucion = Institucion.objects.get(pk=pk, creador=request.user)
            institucion.delete()
            return Response({"detail": "Institucion eliminada correctamente."}, status=status.HTTP_204_NO_CONTENT)
        except Institucion.DoesNotExist:
            return Response({"detail": "Institucion no encontrada o no tienes permisos."}, status=status.HTTP_404_NOT_FOUND)