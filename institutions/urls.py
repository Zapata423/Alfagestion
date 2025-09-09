from django.urls import path
from . import views

urlpatterns = [
    path('instituciones/<int:pk>/', views.InstitucionDetailView.as_view(), name='institucion-detail'),
    path('encargados/<int:pk>/', views.EncargadoDetailView.as_view(), name='encargado-detail'),
]
