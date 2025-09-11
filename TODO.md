# TODO: Modificar CrearValidacionApiView para filtrar actividades por estudiante

- [x] Modificar teachers/urls.py: Agregar estudiante_id a la URL de crear validación
- [x] Modificar teachers/views.py: Capturar estudiante_id en CrearValidacionApiView y pasarlo al serializador
- [x] Modificar teachers/serializers.py: Filtrar queryset de actividad en ValidacionSerializer basado en estudiante_id
- [x] Verificar cambios y probar endpoint
