from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from usuarios.models import Usuarios

# Create your views here.


def bienvenido(request):
    return render(request, 'Inicio/index.html')
    