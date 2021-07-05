from django import forms
from django.contrib.auth import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import fields

class RegistroUsuario(UserCreationForm):
    rut = forms.CharField(max_length=12, help_text="Ingrese Rut")

    class Meta: 
        model = User
        fields = ('rut','username', 'first_name','last_name','email','password1','password2')
