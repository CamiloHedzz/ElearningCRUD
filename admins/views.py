from .forms import CustomUserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model, logout, login



def register(request):
    data = {'form': CustomUserCreationForm()}

    if request.method == 'POST':
        user_creation_form = CustomUserCreationForm(data=request.POST)

        if user_creation_form.is_valid():
            username = user_creation_form.cleaned_data['username']
            email = user_creation_form.cleaned_data['email']
            password = user_creation_form.cleaned_data['password']
   
            user_model = get_user_model()

            # Crear el usuario y guardar directamente en la base de datos
            user = user_model.objects.create_user(username=username, email=email, password=password)

            
            login(request, user)
            return redirect('inicio')
        else:
            data['form'] = user_creation_form

    return render(request, 'Registration/register.html', data)

from cargos.views import CargoForm
from usuarios.views import UserForm
from localizaciones.views import LocaForm
from usuarios.models import Usuarios


@login_required
def inicio(request):
    form_user = UserForm()
    form_loca = LocaForm()
    form_cargo = CargoForm()
    usuarios = Usuarios.objects.all()
    return render(request, 'inicio.html', {'formUser': form_user, 'formLoca': form_loca, 'formCargo': form_cargo,  'usuarios': usuarios})

def exit(request):
    logout(request)
    return redirect('home')