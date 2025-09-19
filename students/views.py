from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (TemplateView)
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from evidence.models import Actividad

class HomePageStudents(LoginRequiredMixin, TemplateView):
    template_name = "students/index.html"
    login_url = reverse_lazy('users_app:estudiantes-login')

# class UploadActividadAPIView(APIView):
#     permission_classes = [IsAuthenticated]

#     def get(self, request):
#         if not hasattr(request.user, "estudiante") or request.user.estudiante is None:
#             return Response({"error": "Usuario no tiene estudiante asociado"}, status=status.HTTP_400_BAD_REQUEST)

#         actividades = Actividad.objects.filter(estudiante=request.user.estudiante)
#         serializer = ActividadSerializer(actividades, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)

#     def post(self, request):
#         if not hasattr(request.user, "estudiante") or request.user.estudiante is None:
#             return Response({"error": "Usuario no tiene estudiante asociado"}, status=status.HTTP_400_BAD_REQUEST)

#         serializer = ActividadSerializer(
#             data=request.data,
#             context={"estudiante": request.user.estudiante}
#         )
#         if serializer.is_valid():
#             actividad = serializer.save()
#             return Response({
#                 "message": "Actividad subida exitosamente",
#                 "id": actividad.id
#             }, status=status.HTTP_201_CREATED)

#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ValidacionesEstadoAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        if not hasattr(request.user, 'estudiante') or request.user.estudiante is None:
            return Response({"error": "Usuario no tiene estudiante asociado"}, status=status.HTTP_400_BAD_REQUEST)

        from reports.models import Validacion
        validaciones = Validacion.objects.filter(actividad__estudiante=request.user.estudiante)
        data = []
        for validacion in validaciones:
            data.append({
                "actividad": str(validacion.actividad),
                "status": validacion.get_status_display(),
                "comentarios": validacion.comentarios,
                "fecha_validacion": validacion.fecha_validacion,
            })
        return Response(data)

class ActividadDetailAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        if not hasattr(request.user, 'estudiante') or request.user.estudiante is None:
            return Response({"error": "Usuario no tiene estudiante asociado"}, status=status.HTTP_400_BAD_REQUEST)

        actividad = get_object_or_404(Actividad, pk=pk, estudiante=request.user.estudiante)
        serializer = ActividadSerializer(actividad)
        return Response(serializer.data)

    def delete(self, request, pk):
        if not hasattr(request.user, 'estudiante') or request.user.estudiante is None:
            return Response({"error": "Usuario no tiene estudiante asociado"}, status=status.HTTP_400_BAD_REQUEST)

        actividad = get_object_or_404(Actividad, pk=pk, estudiante=request.user.estudiante)
        actividad.delete()
        return Response({"message": "Actividad eliminada exitosamente"}, status=status.HTTP_204_NO_CONTENT)
