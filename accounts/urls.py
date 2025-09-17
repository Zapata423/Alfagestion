from django.urls import path
from . import views

app_name = "users_app"

urlpatterns = [
    path('register/', views.UserRegisterView.as_view(), name='user-register'),
    path('home/', views.HomePage.as_view(), name='home'),
    path('loginEstudiantes/', views.LoginUserStudentsAPIView.as_view(), name='estudiantes-login'),
    path('loginDocentes/', views.LoginUserTeachersAPIView.as_view(), name='docentes-login'),
    path('logout/', views.LogoutAPIView.as_view(), name='user-logout'),

]