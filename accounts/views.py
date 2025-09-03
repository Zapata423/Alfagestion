from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import UserLoginForm
from .models import User

def index(request):
    return render(request, 'accounts/index.html', {})

