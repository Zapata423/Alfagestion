from rest_framework.views import APIView
from rest_framework.response import Response
from evidence.models import Actividad
from rest_framework.exceptions import NotFound
from rest_framework import status
from reports.models import Validacion
from rest_framework.permissions import IsAuthenticated
from .serializers import ActividadConEstadoSerializer, ValidacionComentarioSerializer

class ActividadesConEstadoView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        actividades = Actividad.objects.filter(creador=request.user)
        serializer = ActividadConEstadoSerializer(
            actividades, many=True, context={"request": request}
        )
        return Response(serializer.data)
    
class ComentariosPorActividadAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, actividad_id, format=None):
        try:
            validaciones = Validacion.objects.filter(actividad__id=actividad_id)
            
            if not validaciones.exists():
                raise NotFound(detail=f"No se encontraron comentarios para la actividad con ID: {actividad_id}.")

            serializer = ValidacionComentarioSerializer(validaciones, many=True)
        
            return Response(serializer.data, status=status.HTTP_200_OK)

        except NotFound as e:
            return Response({'detail': str(e)}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'detail': 'Ocurrió un error en el servidor.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)