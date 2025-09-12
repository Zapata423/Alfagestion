from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Estudiante
from institutions.models import Institucion, Encargado
from evidence.models import Actividad

User = get_user_model()

class UploadActividadAPITest(APITestCase):
    def setUp(self):
        # Create test data
        self.institucion = Institucion.objects.create(
            nombre="Institucion Test",
            direccion="Calle Test",
            telefono="123456",
            email="test@institucion.com"
        )
        self.encargado = Encargado.objects.create(
            institucion=self.institucion,
            nombre="Encargado",
            apellido="Test",
            correo="encargado@test.com"
        )
        self.estudiante = Estudiante.objects.create(
            nombres="Estudiante",
            apellidos="Test",
            telefono="987654",
            fecha_nacimiento="2000-01-01"
        )
        self.user = User.objects.create_user(
            email="estudiante@test.com",
            password="password123"
        )
        self.user.estudiante = self.estudiante
        self.user.save()

    def test_upload_actividad_authenticated(self):
        self.client.login(email="estudiante@test.com", password="password123")
        url = reverse('students_app:upload-actividad')
        data = {
            'titulo': 'Actividad Test',
            'descripcion': 'Descripción test',
            'horas': 5,
            'institucion': self.institucion.id,
            'encargado': self.encargado.id,
            'archivo': open('requirements/local.txt', 'rb')  # Use existing file for test
        }
        response = self.client.post(url, data, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('message', response.data)
        # Check if actividad was created
        actividad = Actividad.objects.filter(estudiante=self.estudiante).first()
        self.assertIsNotNone(actividad)
        self.assertEqual(actividad.titulo, 'Actividad Test')

    def test_list_actividades_authenticated(self):
        # First create an actividad
        Actividad.objects.create(
            estudiante=self.estudiante,
            institucion=self.institucion,
            encargado=self.encargado,
            titulo='Actividad Lista',
            descripcion='Descripción',
            horas=3
        )
        self.client.login(email="estudiante@test.com", password="password123")
        url = reverse('students_app:upload-actividad')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['titulo'], 'Actividad Lista')

    def test_upload_actividad_unauthenticated(self):
        url = reverse('students_app:upload-actividad')
        data = {
            'titulo': 'Actividad Test',
            'horas': 5,
            'institucion': self.institucion.id,
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
