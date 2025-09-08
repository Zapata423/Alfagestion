from django.urls import path
from . import views

app_name = 'students_app'

urlpatterns = [
    path('panelEstudiantes/', views.HomePageStudents.as_view(), name='panelEstudiantes'),
    # path('logout/', views.logout_view, name='logout'),
    # path('home/', views.home_view, name='home'),
    # path('verificacion/', views.verificacion_view, name='verificacion'),
    # path('mapa/', ListaPersonas.as_view(), name='mapa'),
    # path('calendario/', views.calendario_view, name='calendario'),
    # path('modulo_informativo/', views.modulo_informativo_view, name='modulo_informativo'),
    # path('perfil/', views.perfil_view, name='perfil'),
    # path('registrar_horas/', views.registrar_horas_view, name='registrar_horas'),
    # path('horas_registradas/', views.horas_registradas_view, name='horas_registradas'),
    # path('api/persona/list/', views.PersonListApiView.as_view(),),
    # path('api/persona/create/', views.PersonCreateApiView.as_view(),),
    # path('api/persona/detail/<pk>/', views.PersonDetailView.as_view(),),
    # path('api/persona/delete/<pk>/', views.PersonDeleteView.as_view(),),
    # path('api/persona/update/<pk>/', views.PersonUpdateApiView.as_view(),),
    # path('api/persona/modificar/<pk>/', views.PersonRetrievUpdateApiView.as_view(),),


]

