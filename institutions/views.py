from django.shortcuts import render
from rest_framework.generics import RetrieveAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import Institucion, Encargado
from .serializers import InstitucionSerializer, EncargadoSerializer

# Create your views here.


class InstitucionDetailView(RetrieveAPIView):
    queryset = Institucion.objects.all()
    serializer_class = InstitucionSerializer


class EncargadoDetailView(RetrieveAPIView):
    queryset = Encargado.objects.all()
    serializer_class = EncargadoSerializer


class UploadInstitucionAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = InstitucionSerializer(data=request.data)
        if serializer.is_valid():
            institucion = serializer.save()
            return Response({"message": "Institucion creada exitosamente", "id": institucion.id}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UploadEncargadoAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = EncargadoSerializer(data=request.data)
        if serializer.is_valid():
            encargado = serializer.save()
            return Response({"message": "Encargado creado exitosamente", "id": encargado.id}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



    
