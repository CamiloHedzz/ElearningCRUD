from django.db import models
from localizaciones.models import Localizaciones
from cargos.models import Cargos
# Create your models here.


class Usuarios(models.Model):
    identificacion = models.IntegerField()
    id = models.AutoField(primary_key=True)
    nombres = models.CharField(max_length=500)
    apellidos = models.CharField(max_length=500)
    active = models.BooleanField(default=False)
    localizacion_id = models.ForeignKey(Localizaciones,on_delete=models.SET_NULL,null=True )
    cargo_id = models.ForeignKey(Cargos, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'Localizacion {self.id}: {self.localizacion}: {self.active}'