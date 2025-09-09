from django.urls import path
from . import views


app_name = 'teachers_app'

urlpatterns = [
    path('panelDocentes/', views.HomePageTeachers.as_view(), name='panelDocentes'),
    path('api/grados/lista/', views.ListaGradosApiView.as_view(),),
    path('api/grupos/lista/', views.ListaGruposApiView.as_view(),),
    path('api/estudiantes/', views.ListaEstudiantesPorGradoGrupoApiView.as_view(),),
    path('api/actividades/', views.ListaActividadesPorEstudianteApiView.as_view(),),

]
