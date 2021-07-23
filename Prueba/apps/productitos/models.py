from django.db import models

# Create your models here.

class Productito(models.Model):

    nombre_productito = models.CharField('Producto',
    max_length=50,
    blank=False,
    null=False)
    costo = models.IntegerField('Costo',
    blank=False,
    null=False)
    stock = models.IntegerField('Stock',
    blank=False
    ,null=False
    ,default=0)
    descripcion = models.CharField('Descripcion Producto'
    ,max_length=100,
    blank=False,
    null=False)

    



