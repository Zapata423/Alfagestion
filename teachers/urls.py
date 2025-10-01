from django.urls import path
from . import views


app_name = 'teachers_app'

urlpatterns = [
    path("api/estudiantes/", views.EstudiantesPorGradoGrupoView.as_view(), name="estudiantes-grado-grupo"),
    path("api/estudiante/<int:estudiante_id>/actividades/", views.ActividadesPorEstudianteView.as_view(), name="actividades-por-estudiante"),
    path("api/actividad/<int:actividad_id>/", views.ActividadDetailAPIView.as_view(), name="actividad-detail"),
    path("api/actividades/<int:actividad_id>/institucion/", views.ActividadInstitucionAPIView.as_view(), name="actividad-institucion"),
    path("api/actividades/<int:actividad_id>/encargado/", views.ActividadEncargadoAPIView.as_view(), name="actividad-encargado"),
    path("api/actividades/<int:pk>/validar/", views.ValidarActividadAPIView.as_view(), name="validar-actividad"),
    path("api/actividades/<int:actividad_id>/validacion/editar/", views.EditarValidacionPorActividadView.as_view(), name="editar_validacion_actividad"),
    path("api/actividades/<int:actividad_id>/validacion/", views.ObtenerValidacionPorActividadView.as_view(), name="obtener_validacion_actividad"),
]
