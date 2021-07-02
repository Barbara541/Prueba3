from django.shortcuts import render,redirect
from .forms import RegistroUsuario
from .models import Registro
# Create your views here.
def registro(request):
    return render(request, 'paginas/registro.html')

    
def registro(request):  
    formulario = None
    if request.method == 'POST':
        formulario =  Registro(request.POST)  
        if formulario.is_valid():
            usuario = formulario.save()
            usuario.refresh_from_db()
            usuario.perfil.rut = formulario.cleaned_data.get('rut')
            usuario.save()
            return redirect('paginaprincipal')
        if request.method == 'GET':
            formulario = RegistroUsuario()  
        contexto ={
            'formulario': formulario
        }   

        return render('logeoregister/registro.html', context= contexto)    