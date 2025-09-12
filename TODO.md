# TODO - Implementación de API REST para Subida de Actividades

## Tareas Completadas

### 1. Modelo Institucion
- [x] Agregar campo `creador` a Institucion (ForeignKey a Usuario)

### 2. Serializers
- [x] Crear `institutions/serializers.py` con InstitucionSerializer y EncargadoSerializer
- [x] Actualizar InstitucionSerializer para asignar creador automáticamente en create()
- [x] Crear `students/serializers.py` con ActividadSerializer
- [x] Filtrar querysets de institucion y encargado por creador en ActividadSerializer

### 3. Vistas
- [x] Crear `institutions/views.py` con UploadInstitucionAPIView y UploadEncargadoAPIView
- [x] Crear `students/views.py` con UploadActividadAPIView (GET y POST)
- [x] Agregar ValidacionesEstadoAPIView para ver estado de validaciones

### 4. URLs
- [x] Actualizar `institutions/urls.py` con rutas para upload-institucion y upload-encargado
- [x] Actualizar `students/urls.py` con ruta para upload-actividad
- [x] Incluir `institutions.urls` en `alfagestion/urls.py`

### 5. Configuración
- [x] Agregar MEDIA_URL y MEDIA_ROOT en `alfagestion/settings.py`
- [x] Agregar serving de media en `alfagestion/urls.py`

### 6. Autenticación y Permisos
- [x] Usar IsAuthenticated en todas las vistas API
- [x] Filtrar datos por usuario autenticado (estudiante para actividades, creador para instituciones/encargados)

### 7. Funcionalidad de Eliminación
- [x] Crear ActividadDetailAPIView con métodos GET y DELETE
- [x] Agregar URL para detalle de actividad específica
- [x] Validar que solo el estudiante propietario pueda eliminar su actividad
- [x] Django maneja automáticamente la eliminación del archivo al eliminar el modelo

## Endpoints Disponibles

### Para Estudiantes:
- `POST /api/upload-actividad/` - Subir nueva actividad (titulo, descripcion, archivo, horas, institucion, encargado opcional)
- `GET /api/upload-actividad/` - Listar actividades del estudiante
- `GET /api/upload-actividad/<id>/` - Ver detalle de una actividad específica
- `DELETE /api/upload-actividad/<id>/` - Eliminar una actividad propia
- `GET /api/validaciones-estado/` - Ver estado de validaciones de actividades

### Para Usuarios (crear instituciones/encargados):
- `POST /api/upload-institucion/` - Crear institución
- `POST /api/upload-encargado/` - Crear encargado

## Notas
- La API usa autenticación de sesión y básica
- Los archivos se suben a `media/evidencias/`
- Las instituciones y encargados se filtran por creador
- Las actividades se asignan automáticamente al estudiante del usuario autenticado
