from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (TemplateView, ListView)
from django.urls import reverse_lazy, reverse
from accounts.models import Usuario
from students.models import Estudiante
from evidence.models import Actividad
from reports.models import Validacion
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import ValidationError

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
    ActividadSerializer,
    ValidacionSerializer,
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

class CrearValidacionApiView(CreateAPIView):
    serializer_class = ValidacionSerializer
    queryset = Validacion.objects.all()
    permission_classes = [IsAuthenticated]

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['estudiante_id'] = self.kwargs.get('estudiante_id')
        return context

    def perform_create(self, serializer):
        # Verificar que el usuario tenga rol de docente
        if not self.request.user.rol or self.request.user.rol.nombre.lower() != 'docente':
            raise ValidationError("Solo los docentes pueden crear validaciones.")

        # Verificar que el usuario tenga un perfil de docente asociado
        if not self.request.user.docente:
            raise ValidationError("El usuario no tiene un perfil de docente asociado.")

        # Asignar automáticamente el docente logueado
        docente = self.request.user.docente
        serializer.save(docente=docente)


class ActualizarValidacionApiView(RetrieveUpdateAPIView):
    serializer_class = ValidacionSerializer
    queryset = Validacion.objects.all()
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Filtrar validaciones solo del docente logueado
        return Validacion.objects.filter(docente=self.request.user.docente)

    def perform_update(self, serializer):
        # Verificar que el usuario tenga rol de docente
        if not self.request.user.rol or self.request.user.rol.nombre.lower() != 'docente':
            raise ValidationError("Solo los docentes pueden actualizar validaciones.")

        # Verificar que el usuario tenga un perfil de docente asociado
        if not self.request.user.docente:
            raise ValidationError("El usuario no tiene un perfil de docente asociado.")

        # Asegurar que la validación pertenece al docente logueado
        if serializer.instance.docente != self.request.user.docente:
            raise ValidationError("No tienes permiso para actualizar esta validación.")

        serializer.save()
