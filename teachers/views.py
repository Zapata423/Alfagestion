from reports.models import Validacion
from accounts.models import Usuario
from evidence.models import Actividad
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import status
from django.db import IntegrityError

from .serializers import (
    EstudianteConHorasSerializer,
    ActividadesEstudianteSerializer,
    EvidenciaActividadSerializer,
    EvidenciaEncargadoSerializer,
    EvidenciaInstitucionSerializer,
    ValidacionSerializer
)


class EstudiantesPorGradoGrupoView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        grado = request.query_params.get("grado")
        grupo = request.query_params.get("grupo")

        queryset = Usuario.objects.filter(estudiante__isnull=False)

        if grado:
            queryset = queryset.filter(grado=grado)
        if grupo:
            queryset = queryset.filter(grupo=grupo)

        serializer = EstudianteConHorasSerializer(queryset, many=True)
        return Response(serializer.data)

class ActividadesPorEstudianteView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, estudiante_id):
        # buscamos al estudiante
        estudiante = get_object_or_404(Usuario, id=estudiante_id, estudiante__isnull=False)

        # todas las actividades que el estudiante ha subido
        actividades = Actividad.objects.filter(creador=estudiante)

        # serializamos
        serializer = ActividadesEstudianteSerializer(actividades, many=True)

        return Response(serializer.data)




class ActividadDetailAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, actividad_id):
        actividad = get_object_or_404(Actividad, id=actividad_id)
        serializer = EvidenciaActividadSerializer(actividad, context={"request": request})
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class ActividadInstitucionAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, actividad_id):
        actividad = get_object_or_404(Actividad, id=actividad_id)
        institucion = actividad.institucion
        serializer = EvidenciaInstitucionSerializer(institucion)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ActividadEncargadoAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, actividad_id):
        actividad = get_object_or_404(Actividad, id=actividad_id)
        encargado = actividad.encargado
        serializer = EvidenciaEncargadoSerializer(encargado)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class ValidarActividadAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        actividad = get_object_or_404(Actividad, pk=pk)

        # Evitar duplicados solo por actividad (sin docente)
        if Validacion.objects.filter(actividad=actividad).exists():
            return Response(
                {"error": "Ya existe una validación de esta actividad."},
                status=400
            )

        serializer = ValidacionSerializer(data=request.data)
        if serializer.is_valid():
            try:
                serializer.save(actividad=actividad)  # no docente
                return Response({
                    "success": True,
                    "actividad": actividad.titulo,
                    "status": serializer.data["status"],
                    "comentarios": serializer.data["comentarios"],
                    "fecha_validacion": serializer.data["fecha_validacion"]
                })
            except IntegrityError as e:
                return Response({"error": f"Error de integridad: {str(e)}"}, status=400)
        else:
            return Response(serializer.errors, status=400)
    
class EditarValidacionPorActividadView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request, actividad_id):
        try:
            # buscamos la validación asociada a la actividad
            validacion = Validacion.objects.filter(actividad_id=actividad_id).last()
            if not validacion:
                return Response(
                    {"success": False, "message": "No existe validación para esta actividad"},
                    status=status.HTTP_404_NOT_FOUND
                )

            serializer = ValidacionSerializer(validacion, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    "success": True,
                    "message": "Estado de validación actualizado",
                    "data": serializer.data
                })
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response(
                {"success": False, "message": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
        
class ObtenerValidacionPorActividadView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, actividad_id):
        try:
            validacion = Validacion.objects.filter(actividad_id=actividad_id).last()
            if not validacion:
                return Response(
                    {"error": "No existe validación para esta actividad"},
                    status=status.HTTP_404_NOT_FOUND
                )
            serializer = ValidacionSerializer(validacion)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
