from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import UserLoginForm
from .models import User

def index(request):
    return render(request, 'accounts/index.html', {})

def login_docente_view(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            # Buscar el usuario en nuestro modelo personalizado
            try:
                user_obj = User.objects.get(username=username, password=password, role__name='docente')
                # Crear una sesión manual ya que no usamos el sistema de autenticación de Django
                request.session['user_id'] = user_obj.id
                request.session['username'] = user_obj.username
                request.session['role'] = user_obj.role.name
                messages.success(request, f'Bienvenido docente {username}!')
                return redirect('home_docente')
            except User.DoesNotExist:
                messages.error(request, 'Usuario o contraseña incorrectos, o no tienes permisos de docente')
    else:
        form = UserLoginForm()
    return render(request, 'accounts/login_docente.html', {'form': form})

def login_estudiante_view(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            # Buscar el usuario en nuestro modelo personalizado
            try:
                user_obj = User.objects.get(username=username, password=password, role__name='estudiante')
                # Crear una sesión manual ya que no usamos el sistema de autenticación de Django
                request.session['user_id'] = user_obj.id
                request.session['username'] = user_obj.username
                request.session['role'] = user_obj.role.name
                messages.success(request, f'Bienvenido estudiante {username}!')
                return redirect('home_estudiante')
            except User.DoesNotExist:
                messages.error(request, 'Usuario o contraseña incorrectos, o no tienes permisos de estudiante')
    else:
        form = UserLoginForm()
    return render(request, 'accounts/login_estudiante.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            # Buscar el usuario en nuestro modelo personalizado
            try:
                user_obj = User.objects.get(username=username, password=password)
                # Crear una sesión manual ya que no usamos el sistema de autenticación de Django
                request.session['user_id'] = user_obj.id
                request.session['username'] = user_obj.username
                request.session['role'] = user_obj.role.name
                messages.success(request, f'Bienvenido {username}!')
                return redirect('home')
            except User.DoesNotExist:
                messages.error(request, 'Usuario o contraseña incorrectos')
    else:
        form = UserLoginForm()
    return render(request, 'accounts/login.html', {'form': form})
    
def logout_view(request):
    # Limpiar la sesión personalizada
    if 'user_id' in request.session:
        del request.session['user_id']
    if 'username' in request.session:
        del request.session['username']
    if 'role' in request.session:
        del request.session['role']
    messages.success(request, 'Sesión cerrada correctamente')
    return redirect('index')

def home_view(request):
    # Verificar si el usuario está logueado
    if 'user_id' not in request.session:
        messages.error(request, 'Debes iniciar sesión para acceder a esta página')
        return redirect('index')
    
    context = {
        'username': request.session.get('username'),
        'role': request.session.get('role')
    }
    return render(request, 'accounts/home.html', context)

def home_docente_view(request):
    # Verificar si el usuario está logueado y es docente
    if 'user_id' not in request.session:
        messages.error(request, 'Debes iniciar sesión para acceder a esta página')
        return redirect('index')
    
    if request.session.get('role') != 'docente':
        messages.error(request, 'No tienes permisos para acceder al panel de docentes')
        return redirect('index')
    
    context = {
        'username': request.session.get('username'),
        'role': request.session.get('role')
    }
    return render(request, 'accounts/home_docente.html', context)

def home_estudiante_view(request):
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
    return render(request, 'accounts/home_estudiante.html', context)

