from usuarios.forms import UserForm
from usuarios.models import Usuarios
from django.shortcuts import redirect, render, get_object_or_404

def registerUser(request):
    formUser = UserForm()
    if request.method == 'POST':
        formUser = UserForm(data=request.POST)
        if formUser.is_valid():
            formUser.save()
            return redirect('inicio')            
    else:
        formUser = UserForm
    return redirect('inicio')


def editUser(request, id):
    usuario = get_object_or_404(Usuarios, pk=id)
    if request.method == 'POST':
        formUser = UserForm(request.POST, instance=usuario)
        if formUser.is_valid():
            formUser.save()
            return redirect('inicio')            
    else:
        formUser = UserForm(instance=usuario)
    return render(request, 'usuarios/editUser.html', {'formUser':formUser})


def deleteUser(request, id):
    usuario = Usuarios.objects.get(id=id)
    usuario.delete()
    return redirect('inicio')
    
