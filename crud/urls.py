from django.contrib import admin
from django.urls import path, include
from elearning.views import bienvenido
from cargos.views import registerCargo
from usuarios.views import registerUser, deleteUser, editUser
from localizaciones.views import registerLoca
from admins.views import register, inicio, exit

urlpatterns = [
    #INIT
    path('admin/', admin.site.urls),
    path('', bienvenido, name='home'),
    
    #ADMINS
    path('register/', register, name='register'),
    path('logout/', exit, name='exit'),
    path('inicio/', inicio, name='inicio'),
    path('accounts/', include('django.contrib.auth.urls')),
    
    #USERS
    path('registerUser/', registerUser, name='registerUser'),
    path('registerLoca/', registerLoca, name='registerLoca'),
    path('registerCargo/', registerCargo, name='registerCargo'),
    path('inicio/deleteUser/<identificacion>', deleteUser, name='deleteUser'),
    path('inicio/editUser/<int:id>', editUser, name='editUser'),
    
    
]   
