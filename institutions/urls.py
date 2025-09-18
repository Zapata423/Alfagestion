from django.urls import path
from . import views

urlpatterns = [
    path('instituciones/mias/', views.MisInstitucionesView.as_view(), name='mis-instituciones'),
    path('encargados/mios/', views.MisEncargadosView.as_view(), name='mis-encargados'),
    path('api/upload-institucion/', views.UploadInstitucionAPIView.as_view(), name='upload-institucion'),
    path('api/upload-encargado/', views.UploadEncargadoAPIView.as_view(), name='upload-encargado'),
    path('encargados/<int:pk>/delete/', views.DeleteEncargadoView.as_view(), name='borrar-encargado'),
    path('instituciones/<int:pk>/delete/', views.DeleteInstitucionView.as_view(), name='borrar-institucion')
]
