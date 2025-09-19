from django.urls import path
from . import views

urlpatterns = [
    path('api/upload-actividad/', views.UploadActividadAPIView.as_view(), name='upload-actividad'),
]

