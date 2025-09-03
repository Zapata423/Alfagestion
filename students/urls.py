from django.urls import path
from . import views

app_name = 'students'

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('home/', views.home_view, name='home'),
    path('verificacion/', views.verificacion_view, name='verificacion'),
    path('mapa/', views.mapa_view, name='mapa'),
    path('calendario/', views.calendario_view, name='calendario'),
    path('modulo_informativo/', views.modulo_informativo_view, name='modulo_informativo'),
    path('perfil/', views.perfil_view, name='perfil'),
    path('registrar_horas/', views.registrar_horas_view, name='registrar_horas'),
    path('horas_registradas/', views.horas_registradas_view, name='horas_registradas'),
]