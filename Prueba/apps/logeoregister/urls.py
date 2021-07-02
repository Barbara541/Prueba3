from apps.logeoregister.forms import RegistroUsuario
from django import urls
from django.urls import path
from . import views
from .views import registro

urlpatterns = [
    path('registro/', views.registro, name='registro'),
    ##path('registro/', views.registro, name='registro'),
]


