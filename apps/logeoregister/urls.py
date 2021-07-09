from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import templatize
from apps.logeoregister.forms import RegistroUsuario
from django import urls
from django.urls import path
from .import views
from .views import registro,salir
from .forms import IniciarSesion
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('registro/', views.registro, name='registro'),
    path('iniciar-sesion/',LoginView.as_view(
    template_name='paginas/iniciarSesion.html',
    authentication_form = IniciarSesion
    ), name='IniciarSesion'),
    path('salir/',salir),
    path('iniciar-sesion/',IniciarSesion, name='iniciar_sesion')
    ##path('registro/', views.registro, name='registro'),
]


