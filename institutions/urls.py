from django.urls import path
from . import views

urlpatterns = [
    path('instituciones/<int:pk>/', views.InstitucionDetailView.as_view(), name='institucion-detail'),
    path('encargados/<int:pk>/', views.EncargadoDetailView.as_view(), name='encargado-detail'),
    path('api/upload-institucion/', views.UploadInstitucionAPIView.as_view(), name='upload-institucion'),
    path('api/upload-encargado/', views.UploadEncargadoAPIView.as_view(), name='upload-encargado'),
]
