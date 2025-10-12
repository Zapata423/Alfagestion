AlfaGestion – Backend
PROFE O PERSONA QUE DESEA DESCARGAR Y USAR EL SOFTWARE AQUI ESTAN LAS ESPECIFICACIONES E INDICACIONES:

AlfaGestion es una plataforma de gestión de servicio social estudiantil,
 desarrollada en Django + Django REST Framework. 
 Permite administrar estudiantes, docentes, instituciones, actividades y validaciones de servicio social.


 ✅ Instalación y Ejecución(PARA BEDOYA Y GATO):

•	Cambiar el puerto : 5433 -> 5432

•	Crear entorno virtual e instalar dependencias:
 python -m venv venv
 venv\Scripts\activate      
pip install -r requirements/local.txt

•	Aplicar migraciones:
 python manage.py makemigrations
 python manage.py migrate

•	Crear superusuario:
 python manage.py createsuperuser

•	Ejecutar servidor:
 python manage.py runserver

 El proyecto estará disponible en: http://127.0.0.1:8000/



⚠️ Configuración Inicial Obligatoria

Antes de iniciar el uso del sistema, es necesario realizar la siguiente configuración desde el panel de administración de Django (/admin):

Crear un Superusuario o Administrador
Este usuario será el encargado de gestionar los roles y usuarios iniciales.
Se puede crear desde la terminal o el panel de administración:

python manage.py createsuperuser

Luego ingresar a:
👉 http://127.0.0.1:8000/admin/

Crear los Roles del Sistema
Dentro del modelo Rol, deben crearse los siguientes registros:

Estudiante
Docente

Estos roles son fundamentales para el funcionamiento del sistema, ya que determinan los permisos y vistas que cada usuario tendrá dentro de la plataforma.



✅ Estructura de Apps:
* accounts: Maneja el registro, login y logout de usuarios. Soporta roles: Estudiante y Docente.

* institutions: Administra las instituciones educativas y sus encargados.

* students: Permite a los estudiantes subir actividades, consultar validaciones y gestionar sus actividades.

* teachers: Permite a los docentes consultar estudiantes, actividades y emitir validaciones.

(También incluye apps auxiliares como evidence y reports que soportan la gestión de actividades y validaciones).





✅ APIs REST de AlfaGestion

# Accounts 
* POST /api/estudiante/registro → Registrar un nuevo Estudiante (Ruta usada por Admin/Director).
* POST /api/docente/registro → Registrar un nuevo Docente (Ruta usada por Admin/Director).
* POST /api/loginEstudiantes/ → Login para usuarios con rol Estudiante.
* POST /api/loginDocentes/ → Login para usuarios con rol Docente.
* POST /api/loginAdmin/ → Login para usuarios con rol Administrador.
* POST /logout/ → Logout de sesión (invalida el token).

--------------------------------------

# Students 
* GET /api/perfil/estudiante/ → Obtener el Perfil detallado del estudiante autenticado.
* POST /api/upload-actividad/ → Subir una nueva actividad de servicio social (incluye archivo).
* GET /api/actividades/mias/ → Listar todas las actividades del estudiante autenticado.
* DELETE /api/actividad/<id>/delete/ → Eliminar una actividad de servicio social específica.
* GET /api/validaciones/mias/ → Consultar estados de Validación recibidas.

--------------------------------------

# Institutions (Instituciones y Encargados)
* POST /api/upload-institucion/ → Crear/Subir una nueva Institución.
* POST /api/upload-encargado/ → Crear/Subir un nuevo Encargado de Institución.
* GET /instituciones/mias/ → Listar las instituciones asociadas al usuario autenticado.
* GET /api/encargados/mios/ → Listar los encargados asociados al usuario autenticado.
* DELETE /api/instituciones/<id>/delete/ → Borrar una Institución específica.
* DELETE /encargados/<id>/delete/ → Borrar un Encargado específico.

--------------------------------------

# Teachers
* GET /api/estudiantes/?grado=<val>&grupo=<val> → Listar estudiantes filtrados por Grado y Grupo.
* GET /api/estudiante/<id>/actividades/ → Listar todas las actividades de un estudiante específico (por su ID).
* PUT/PATCH /api/actividades/<id>/validacion/editar/ → Actualizar o modificar el estado y comentarios de una validación.
* GET /api/actividades/<id>/institucion/ → Detalle de Institución asociada a una actividad específica.
* GET /api/actividades/<id>/encargado/ → Detalle de Encargado asociado a una actividad específica.
* POST /api/actividades/<id>/validacion/crear/  → Crear validación.
