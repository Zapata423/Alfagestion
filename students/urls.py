from django.urls import path
from . import views

app_name = 'students_app'

urlpatterns = [
    path('panelEstudiantes/', views.HomePageStudents.as_view(), name='panelEstudiantes'),
    path('api/upload-actividad/', views.UploadActividadAPIView.as_view(), name='upload-actividad'),
    path('api/upload-actividad/<int:pk>/', views.ActividadDetailAPIView.as_view(), name='actividad-detail'),
    path('api/validaciones-estado/', views.ValidacionesEstadoAPIView.as_view(), name='validaciones-estado'),


]

