from django.shortcuts import render

# Create your views here.

def principal(request):
    return render(request, 'paginas/index.html') 

def galeria(request):
    return render(request,'paginas/Galeria.html')

def producto(request):
    return render(request,'paginas/Productos.html')

    