from django.shortcuts import redirect
from django.forms import modelform_factory
from localizaciones.models import Localizaciones

LocaForm = modelform_factory(Localizaciones, exclude=[])


def registerLoca(request):
    formLoca = LocaForm()
    if request.method == 'POST':
        formLoca = LocaForm(data=request.POST)
        if formLoca.is_valid():
            formLoca.save()            
    else:
        formLoca = LocaForm
    return redirect('inicio')