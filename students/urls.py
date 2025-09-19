from django.urls import path
from . import views

app_name = 'students_app'

urlpatterns = [
    path('panelEstudiantes/', views.HomePageStudents.as_view(), name='panelEstudiantes'),



]

