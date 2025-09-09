from django.shortcuts import render
from rest_framework.generics import RetrieveAPIView
from .models import Institucion, Encargado
from .serializers import InstitucionSerializer, EncargadoSerializer

# Create your views here.


class InstitucionDetailView(RetrieveAPIView):
    queryset = Institucion.objects.all()
    serializer_class = InstitucionSerializer


class EncargadoDetailView(RetrieveAPIView):
    queryset = Encargado.objects.all()
    serializer_class = EncargadoSerializer


    
