from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path('login/docente/', views.login_docente_view, name='login_docente'),
    path('login/estudiante/', views.login_estudiante_view, name='login_estudiante'),
    path('logout/', views.logout_view, name='logout'),
    path('home/', views.home_view, name='home'),
    path('home/docente/', views.home_docente_view, name='home_docente'),
    path('home/estudiante/', views.home_estudiante_view, name='home_estudiante'),
]