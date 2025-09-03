from django.shortcuts import render, redirect
from django.contrib import messages
from accounts.forms import UserLoginForm
from accounts.models import User


def login_view(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            # Buscar el usuario en nuestro modelo personalizado
            try:
                user_obj = User.objects.get(username=username, password=password, role__name='estudiante')
                
                # Limpiar mensajes existentes antes de crear la sesión
                from django.contrib.messages import get_messages
                list(get_messages(request))
                
                # Crear una sesión manual ya que no usamos el sistema de autenticación de Django
                request.session['user_id'] = user_obj.id
                request.session['username'] = user_obj.username
                request.session['role'] = user_obj.role.name
                messages.success(request, f'Bienvenido estudiante {username}!')
                return redirect('students:home')
            except User.DoesNotExist:
                messages.error(request, 'Usuario o contraseña incorrectos, o no tienes permisos de estudiante')
    else:
        form = UserLoginForm()
    return render(request, 'students/login.html', {'form': form})


def logout_view(request):
    # Limpiar la sesión personalizada
    if 'user_id' in request.session:
        del request.session['user_id']
    if 'username' in request.session:
        del request.session['username']
    if 'role' in request.session:
        del request.session['role']
    
    # Limpiar todos los mensajes existentes
    from django.contrib.messages import get_messages
    list(get_messages(request))
    
    messages.success(request, 'Sesión cerrada correctamente')
    return redirect('index')



def home_view(request):
    # Verificar si el usuario está logueado y es estudiante
    if 'user_id' not in request.session:
        messages.error(request, 'Debes iniciar sesión para acceder a esta página')
        return redirect('index')
    
    if request.session.get('role') != 'estudiante':
        messages.error(request, 'No tienes permisos para acceder al panel de estudiantes')
        return redirect('index')
    
    context = {
        'username': request.session.get('username'),
        'role': request.session.get('role')
    }
    return render(request, 'students/home.html', context)


def verificacion_view(request):
    return render(request, 'students/verificacion.html')


def mapa_view(request):
    return render(request, 'students/mapa.html')


def calendario_view(request):
    return render(request, 'students/calendario.html')


def modulo_informativo_view(request):
    return render(request, 'students/modulo_informativo.html')


def perfil_view(request):
    return render(request, 'students/perfil.html')


def registrar_horas_view(request):
    return render(request, 'students/registrar_horas.html')


def horas_registradas_view(request):
    return render(request, 'students/horas_registradas.html')