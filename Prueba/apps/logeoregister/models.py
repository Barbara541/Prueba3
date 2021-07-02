from django.contrib.auth.models import User
from django.db import models
from django.utils import tree
from django.dispatch import receiver
from django.db.models.signals import post_save
# Create your models here.

class Registro(models.Model):
    nombre_Usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    fecha_Creacion = models.DateTimeField(auto_now_add=True)
  

    def __str__(self):
       return self.usuario.username
     
    @receiver(post_save, sender=User)
    def actualizar_perfil(sender, instance, created, **kwargs):
        if created: 
            Registro.objects.created(usuario = instance)
        instance.perfil.save()      
