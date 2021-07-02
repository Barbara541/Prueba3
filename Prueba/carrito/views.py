from django.shortcuts import redirect, render
from .carro import Carro

# Create your views here.

def agregar_producto(request, producto_id):
    carro=Carro(request)
    producto=producto.objects.get(id=producto_id)
    carro.agregar(producto=producto)
    return redirect("Prueba")

def eliminar_producto(request, producto_id):
    carro=Carro(request)
    producto=producto.objects.get(id=producto_id)
    carro.eliminar(producto=producto)
    return redirect("Prueba")

def restar_producto(request, producto_id):
    carro=Carro(request)
    producto=producto.objects.get(id=producto_id)
    carro.restar_producto(producto=producto)
    return redirect("Prueba")

def limpiar_carro(request, producto_id):
    carro=Carro(request)
    carro.limpiar_carro()
    return redirect("Prueba")