from django.urls import path
from . import views

app_name = "users_app"

urlpatterns = [
    path('register/', views.UserRegisterView.as_view(), name='user-register'),
    path('home/', views.HomePage.as_view(), name='home'),
    path('loginEstudiantes/', views.LoginUserStudents.as_view(), name='estudiantes-login'),
    path('loginDocentes/', views.LoginUserTeachers.as_view(), name='docentes-login'),
    path('logout/', views.LogoutView.as_view(), name='user-logout'),

]