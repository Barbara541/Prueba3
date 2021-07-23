from django.shortcuts import render

# Create your views here.

def Agregaproductos(request):
   return render (request,'paginas/AgregarProducto.html')