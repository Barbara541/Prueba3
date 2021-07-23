from django.urls import path
from .views import Agregaproductos
urlpatterns = [
    path('AgregarProducto/',Agregaproductos,name='agregarproducto')
]
