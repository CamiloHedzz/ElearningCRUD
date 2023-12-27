from cargos.models import Cargos
from django.forms import modelform_factory
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render, render, get_object_or_404
from django.contrib.auth import get_user_model, logout, login

CargoForm = modelform_factory(Cargos, exclude=[])

def registerCargo(request):
    formCargo = CargoForm()
    if request.method == 'POST':
        formCargo = CargoForm(data=request.POST)
        if formCargo.is_valid():
            formCargo.save()            
    else:
        formCargo = CargoForm
    return redirect('inicioCargos')


@login_required
def inicioCargos(request):
    form_cargo = CargoForm()
    cargos = Cargos.objects.all()
    return render(request, 'cargos/cargos.html', {'formCargo': form_cargo,  'cargos': cargos})    


def editCargo(request, id):
    cargo = get_object_or_404(Cargos, pk=id)
    if request.method == 'POST':
        formCargo = CargoForm(request.POST, instance=cargo)
        if formCargo.is_valid():
            formCargo.save()
            return redirect('inicioCargos')            
    else:
        formCargo = CargoForm(instance=cargo)
    return render(request, 'cargos/editCargos.html', {'formCargo':formCargo})


def deleteCargo(request, id):
    cargo = Cargos.objects.get(id=id)
    cargo.delete()
    return redirect('inicioCargos')