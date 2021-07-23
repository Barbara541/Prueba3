from os import name
from django.urls import path
from . import views


urlpatterns = [
    path('', views.principal, name='principal'),
    path('Galeria/', views.galeria, name='galeria'),
    path('productos/', views.productos, name='productos'),
    path('index/', views.index, name='index'),
    path('AcercadeNosotros/', views.acercadenosotros, name='AcercadeNosotros'),

]

