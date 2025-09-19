from django.urls import path
from . import views

urlpatterns = [
    path('api/instituciones/mias/', views.MisInstitucionesView.as_view(), name='mis-instituciones'),
    path('api/encargados/mios/', views.MisEncargadosView.as_view(), name='mis-encargados'),
    path('api/upload-institucion/', views.UploadInstitucionAPIView.as_view(), name='upload-institucion'),
    path('api/upload-encargado/', views.UploadEncargadoAPIView.as_view(), name='upload-encargado'),
    path('api/encargados/<int:pk>/delete/', views.DeleteEncargadoView.as_view(), name='borrar-encargado'),
    path('api/instituciones/<int:pk>/delete/', views.DeleteInstitucionView.as_view(), name='borrar-institucion')
]
