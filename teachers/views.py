from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (TemplateView)
from django.urls import reverse_lazy, reverse

class HomePageTeachers(LoginRequiredMixin, TemplateView):
    template_name = "teachers/index.html"
    login_url = reverse_lazy('users_app:docentes-login')
