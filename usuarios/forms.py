from cargos.models import Cargos
from usuarios.models import Usuarios
from localizaciones.models import Localizaciones
from django.forms import ModelForm, EmailInput, TextInput

class UserForm (ModelForm):
    
    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)

        active_localizaciones = Localizaciones.objects.filter(active=True)
        self.fields['localizacion_id'].queryset = active_localizaciones
        
        active_cargos = Cargos.objects.filter(active=True)
        self.fields['cargo_id'].queryset = active_cargos
    
    class Meta:
        model = Usuarios
        fields = '__all__'
        widget = {
            'email': EmailInput(attrs ={'type':'email'}),
            'localizacion_id': TextInput(attrs ={'type':'text'}),
            'cargo_id': TextInput(attrs ={'type':'text'})
        }
        
        