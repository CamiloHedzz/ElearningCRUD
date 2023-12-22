from usuarios.models import Usuarios
from django.shortcuts import redirect, render, get_object_or_404
from django.forms import modelform_factory

UserForm = modelform_factory(Usuarios, exclude=[])

def registerUser(request):
    formUser = UserForm()
    if request.method == 'POST':
        formUser = UserForm(data=request.POST)
        if formUser.is_valid():
            formUser.save()            
    else:
        formUser = UserForm
    return redirect('inicio')


def editUser(request, id):
    formUser = UserForm()
    if request.method == 'POST':
        formUser = UserForm(data=request.POST)
        if formUser.is_valid():
            formUser.save()            
    else:
        usuario = get_object_or_404(Usuarios, pk=id)
        formUser = UserForm(instance=usuario)
    return render(request, 'Crud/editUser.html', {'formUser':formUser})


def deleteUser(request, identificacion):
    
    usuario = Usuarios.objects.get(identificacion=identificacion)
    usuario.delete()
    return redirect('inicio')
    
