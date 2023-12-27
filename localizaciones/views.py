from django.forms import modelform_factory
from localizaciones.models import Localizaciones
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render, render, get_object_or_404

LocaForm = modelform_factory(Localizaciones, exclude=[])

def registerLoca(request):
    formLoca = LocaForm()
    if request.method == 'POST':
        formLoca = LocaForm(data=request.POST)
        if formLoca.is_valid():
            formLoca.save()            
    else:
        formLoca = LocaForm
    return redirect('inicioLoca')


@login_required
def inicioLoca(request):
    form_loca = LocaForm()
    localizaciones = Localizaciones.objects.all()
    return render(request, 'localizaciones/localizaciones.html', {'formLocal': form_loca,  'localizaciones': localizaciones})    


def editLoca(request, id):
    localizacion = get_object_or_404(Localizaciones, pk=id)
    if request.method == 'POST':
        formLoca = LocaForm(request.POST, instance=localizacion)
        if formLoca.is_valid():
            formLoca.save()
            return redirect('inicioLoca')            
    else:
        formLoca = LocaForm(instance=localizacion)
    return render(request, 'localizaciones/editLocalizaciones.html', {'formLoca':formLoca})


def deleteLoca(request, id):
    localizacion = Localizaciones.objects.get(id=id)
    localizacion.delete()
    return redirect('inicioLoca')