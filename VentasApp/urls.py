from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from .views import *

urlpatterns = [
    path('add_item',add_item,name='add_item'),
    path('inicio/',inicio,name='inicio'),
    path('cerrar_sesion/',cerrarSesion,name='cerrar_sesion'),
    path('delete_item/<int:myid>',delete_item,name='delete_item'),
    path('listadoproducto/',listadoproducto,name='listadoproducto'),
]