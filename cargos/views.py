from cargos.models import Cargos
from django.shortcuts import redirect
from django.forms import modelform_factory

CargoForm = modelform_factory(Cargos, exclude=[])

def registerCargo(request):
    formCargo = CargoForm()
    if request.method == 'POST':
        formCargo = CargoForm(data=request.POST)
        if formCargo.is_valid():
            formCargo.save()            
    else:
        formCargo = CargoForm
    return redirect('inicio')
    