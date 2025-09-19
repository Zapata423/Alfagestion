from rest_framework.views import APIView
from rest_framework.response import Response
from evidence.models import Actividad
from rest_framework.permissions import IsAuthenticated
from .serializers import ActividadConEstadoSerializer

class ActividadesConEstadoView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        actividades = Actividad.objects.filter(creador=request.user)
        serializer = ActividadConEstadoSerializer(
            actividades, many=True, context={"request": request}
        )
        return Response(serializer.data)