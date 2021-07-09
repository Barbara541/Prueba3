from django.http import request
from django.shortcuts import render
from django.contrib import messages

# Create your views here.

## Tipos de mensajes

##def principal(request):
  ##  messages.debug(request, 'Este es un mensaje de debug')
  ##  messages.info(request, 'Este es un mensaje de info')
  ##  messages.success(request, 'Este es un mensaje de success')
  ##  messages.warning(request, 'Este es un mensaje de warning')
  ##  messages.error(request, 'Este es un mensaje de error')
  ##  messages.add_message(request, messages.ERROR, 'mensaje de error')
   ## return render(request,'paginas/index.html') 

def galeria(request):
    return render(request,'paginas/Galeria.html')

def productos(request):
    return render(request,'paginas/Productos.html')

def index (request):
    return render(request,'base.html')

def acercadenosotros(request):  
    return render(request,'paginas/Acerca de nosotros.html')    

def agregarproducto(request):
    return render(request,'paginas/Agregar Producto.html')

def principal(request):
    return render(request,'paginas/index.html' )


