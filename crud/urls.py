from django.contrib import admin
from django.urls import path, include
from elearning.views import bienvenido
from admins.views import register, inicio, exit
from usuarios.views import registerUser, deleteUser, editUser
from cargos.views import registerCargo, inicioCargos, editCargo, deleteCargo
from localizaciones.views import inicioLoca, registerLoca, editLoca, deleteLoca

urlpatterns = [
    #INIT
    path('admin/', admin.site.urls),
    path('', bienvenido, name='home'),
    
    #ADMINS
    path('logout/', exit, name='exit'),
    path('register/', register, name='register'),
    path('accounts/', include('django.contrib.auth.urls')),
    
    #USERS
    path('inicio/', inicio, name='inicio'),
    path('registerUser/', registerUser, name='registerUser'),
    path('inicio/editUser/<int:id>', editUser, name='editUser'),
    path('inicio/deleteUser/<int:id>', deleteUser, name='deleteUser'),
    
    #CARGOS
    path('inicioCargos/', inicioCargos, name='inicioCargos'),
    path('registerCargo/', registerCargo, name='registerCargo'),
    path('inicioCargos/editCargo/<int:id>', editCargo, name='editCargo'),
    path('inicioCargos/deleteCargo/<int:id>', deleteCargo, name='deleteCargo'),
    
    #LOCALIZACIONES
    path('inicioLoca/', inicioLoca, name='inicioLoca'),
    path('registerLoca/', registerLoca, name='registerLoca'),
    path('inicioLoca/editLoca/<int:id>', editLoca, name='editLoca'),
    path('inicioLoca/deleteLoca/<int:id>', deleteLoca, name='deleteLoca'),
       
]   
