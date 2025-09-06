from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
# from .forms import UserLoginForm
from .models import Usuario

def index(request):
    return render(request, 'accounts/index.html', {})

