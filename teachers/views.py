from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (TemplateView, ListView)
from django.urls import reverse_lazy, reverse
from accounts.models import Usuario
from students.models import Estudiante
from evidence.models import Actividad

from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView,
    DestroyAPIView,
    UpdateAPIView,
    RetrieveUpdateAPIView,
)

from .serializers import (
    GrupoSerializer,
    GradoSerializer,
    EstudianteSerializer,
    ActividadSerializer
)

class HomePageTeachers(LoginRequiredMixin, TemplateView):
    template_name = "teachers/index.html"
    login_url = reverse_lazy('users_app:docentes-login')
    

class ListaGradosApiView(ListAPIView):
    serializer_class = GradoSerializer

    def get_queryset(self):
        return Usuario.objects.exclude(grado__isnull=True).values('grado').distinct()
    

class ListaGruposApiView(ListAPIView):
    serializer_class = GrupoSerializer

    def get_queryset(self):
        return Usuario.objects.exclude(grupo__isnull=True).values('grupo').distinct()




class ListaEstudiantesPorGradoGrupoApiView(ListAPIView):
    serializer_class = EstudianteSerializer

    def get_queryset(self):
        grado = self.request.query_params.get('grado')
        grupo = self.request.query_params.get('grupo')
        queryset = Usuario.objects.filter(rol__nombre='Estudiante')
        if grado:
            queryset = queryset.filter(grado=grado)
        if grupo:
            queryset = queryset.filter(grupo=grupo)
        return queryset


class ListaActividadesPorEstudianteApiView(ListAPIView):
    serializer_class = ActividadSerializer

    def get_queryset(self):
        estudiante_id = self.request.query_params.get('estudiante_id')
        if estudiante_id:
            return Actividad.objects.filter(estudiante_id=estudiante_id)
        return Actividad.objects.none()

