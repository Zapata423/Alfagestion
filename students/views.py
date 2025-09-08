from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (TemplateView)

class HomePageStudents(LoginRequiredMixin, TemplateView):
    template_name = "students/index.html"
    login_url = reverse_lazy('users_app:estudiantes-login')