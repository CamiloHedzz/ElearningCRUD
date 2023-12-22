from django.db import models

# Create your models here.


class Localizaciones(models.Model):
    id = models.AutoField(primary_key=True)
    localizacion = models.CharField(max_length=500)
    active = models.BooleanField(default=False)

    def __str__(self):
        return f'Localizacion {self.id}: {self.localizacion}: {self.active}'