from django.db import models

# Create your models here.

class Cargos(models.Model):
    id = models.AutoField(primary_key=True)
    cargo = models.CharField(max_length=500)
    active = models.BooleanField(default=False)

    def __str__(self):
        return f'Cargo {self.id}: {self.cargo}: {self.active}'