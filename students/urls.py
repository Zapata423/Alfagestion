from django.urls import path
from . import views

app_name = 'students_app'

urlpatterns = [
    path('panelEstudiantes/', views.HomePageStudents.as_view(), name='panelEstudiantes'),
    # path('api/persona/list/', views.PersonListApiView.as_view(),),
    # path('api/persona/create/', views.PersonCreateApiView.as_view(),),
    # path('api/persona/detail/<pk>/', views.PersonDetailView.as_view(),),
    # path('api/persona/delete/<pk>/', views.PersonDeleteView.as_view(),),
    # path('api/persona/update/<pk>/', views.PersonUpdateApiView.as_view(),),
    # path('api/persona/modificar/<pk>/', views.PersonRetrievUpdateApiView.as_view(),),


]

