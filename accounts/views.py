from django.shortcuts import render, redirect
from django.views.generic import ( CreateView, TemplateView, View)
from django.views.generic.edit import ( FormView)
from .models import Usuario
from .forms import UserRegisterForm, LoginForm
from django.urls import reverse_lazy, reverse
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect

class HomePage(TemplateView):
    template_name = "users/home.html"

class UserRegisterView(FormView):
    template_name = 'users/register.html'
    form_class = UserRegisterForm
    success_url = '/'

    def form_valid(self, form):
        Usuario.objects.create_user(
            form.cleaned_data['email'],
            form.cleaned_data['password1'],
            rol=form.cleaned_data['rol'],
            estudiante=form.cleaned_data['estudiante'],
            docente=form.cleaned_data['docente'],

            cargo=form.cleaned_data['cargo'],
            grado=form.cleaned_data['grado'],

        )

        
        return super(UserRegisterView, self).form_valid(form)

class LoginUserStudents(FormView):
    template_name = 'students/login.html'
    form_class = LoginForm
    success_url = reverse_lazy('students_app:panelEstudiantes')
    
    def form_valid(self, form):
        user = authenticate(
            email=form.cleaned_data['email'],
            password=form.cleaned_data['password'],
        )
        if user is not None:
            if user.rol.nombre.lower() == "estudiante":
                login(self.request, user)
                return super(LoginUserStudents, self).form_valid(form)
            else:
                form.add_error(None, "Solo los estudiantes pueden iniciar sesión aquí.")
                return self.form_invalid(form)
        else:
            form.add_error(None, "Credenciales inválidas.")
            return self.form_invalid(form)
        
class LoginUserTeachers(FormView):
    template_name = 'teachers/login.html'
    form_class = LoginForm
    success_url = reverse_lazy('teachers_app:panelDocentes')
    
    def form_valid(self, form):
        user = authenticate(
            email=form.cleaned_data['email'],
            password=form.cleaned_data['password'],
        )
        if user is not None:
            if user.rol.nombre.lower() == "docente":
                login(self.request, user)
                return super(LoginUserTeachers, self).form_valid(form)
            else:
                form.add_error(None, "Solo los Docentes pueden iniciar sesión aquí.")
                return self.form_invalid(form)
        else:
            form.add_error(None, "Credenciales inválidas.")
            return self.form_invalid(form)
        
class LogoutView(View):

    def get(set, request, *args, **kargs):
        logout(request)
        return HttpResponseRedirect(
            reverse(
                'users_app:home'
            )
        )

