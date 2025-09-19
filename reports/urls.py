from django.urls import path
from . import views

urlpatterns = [
    path('api/validaciones/mias/', views.ActividadesConEstadoView.as_view(), name='mis-Validaciones'),
]
