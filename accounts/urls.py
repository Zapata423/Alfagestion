from django.urls import path
from . import views

app_name = "users_app"

urlpatterns = [
    path('register/', views.UserRegisterView.as_view(), name='user-register'),
    path('home/', views.HomePage.as_view(), name='home'),
    path('api/loginEstudiantes/', views.LoginUserStudentsAPIView.as_view(), name='estudiantes-login'),
    path('api/loginDocentes/', views.LoginUserTeachersAPIView.as_view(), name='docentes-login'),
    path('api/loginAdmin/', views.LoginUserAdminAPIView.as_view(), name='admin-login'),
    path('api/logout/', views.LogoutAPIView.as_view(), name='user-logout'),
    path('api/estudiante/registro', views.EstudianteRegistroCompletoAPIView.as_view(), name='registrar-estudiante'),
    path('api/docente/registro', views.DocenteRegistroCompletoAPIView.as_view(), name='registrar-docente'),

]