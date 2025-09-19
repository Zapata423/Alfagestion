from django.urls import path
from . import views

urlpatterns = [
    path('api/upload-actividad/', views.UploadActividadAPIView.as_view(), name='upload-actividad'),
    path('api/actividad/<int:pk>/delete/', views.DeleteActividadView.as_view(), name='borrar-actividad'),
    path('api/actividades/mias/', views.MisActividadesView.as_view(), name='mis-actividades'),
]

