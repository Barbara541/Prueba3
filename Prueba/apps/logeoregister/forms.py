from django import forms
from django.contrib.auth import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import fields

class RegistroUsuario(UserCreationForm):
    

    class Meta: 
        model = User
        fields = ('username', 'first_name','last_name','email','password1','password2')