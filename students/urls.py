from django.urls import path
from . import views

app_name = 'students_app'

urlpatterns = [
        path('api/perfil/estudiante/', views.EstudiantePerfilAPIView.as_view(), name='estudiante-perfil'),

]

