from django.shortcuts import render,redirect
from .forms import RegistroUsuario
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
# Create your views here.
def registro(request):
    return render(request, 'paginas/registro.html')

def IniciarSesion(request):
    formulario = None
    if request.method == 'GET':
        formulario = IniciarSesion(request)
    if request.method == 'POST':
        usuario = request.POST['username']
        contrasena = request.POST['password']
        usuario = authenticate(username=usuario, password = contrasena)
        if usuario is not None:
            login(request, usuario)
            return redirect('principal')

def salir(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('principal')
    
def registro(request):  
    formulario = None
    if request.method == 'POST':
        formulario =  RegistroUsuario(request.POST)  
        if formulario.is_valid():
            username = formulario.cleaned_data['username']
            ##usuario = formulario.save()
            ##usuario.refresh_from_db()
            formulario.save()
            messages.success(request, 'Usuario {} Usuario Registrado'.format(
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


   