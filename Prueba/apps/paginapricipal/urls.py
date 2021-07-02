from django.urls import path
from . import views


urlpatterns = [
    path('', views.principal, name='principal'),
    path('galeria/', views.galeria, name='galeria'),
    path('/productos', views.productos, name='productos')
]

