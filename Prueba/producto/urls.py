from django.urls import path
from .views import vistaPrincipal
urlpatterns=[
    path('', vistaPrincipal)
]