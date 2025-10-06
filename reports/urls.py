from django.urls import path
from . import views


urlpatterns = [
    path('api/validaciones/mias/', views.ActividadesConEstadoView.as_view(), name='mis-Validaciones'),
    path('api/comentarios/<int:actividad_id>/', views.ComentariosPorActividadAPIView.as_view(), name='comentarios-por-actividad'),
]
