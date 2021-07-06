from django.shortcuts import render,redirect
from .forms import RegistroUsuario
from .models import Registro
from django.contrib import messages
# Create your views here.
def registro(request):
    return render(request, 'paginas/registro.html')

    
def registro(request):  
    formulario = None
    if request.method == 'POST':
        formulario =  RegistroUsuario(request.POST)  
        if formulario.is_valid():
            username = formulario.cleaned_data['username']
            ##usuario = formulario.save()
            ##usuario.refresh_from_db()
            formulario.save()
            messages.success(request, 'Usuario {} Registrado correctamente'.format(
                username
            ))
            return redirect('principal')
        else:
            messages.info(request, 'Formulario incompleto, Completelo por Favor')    
        
            
    if request.method == 'GET':
        formulario = RegistroUsuario()  
    contexto  ={
        'formulario': formulario
    }   

    return render(request,'paginas/registro.html',  contexto)    