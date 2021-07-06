from django.db import models

# Create your models here.
class Producto(models.Model):
    nombre_producto = models.CharField('Nombre Producto', max_length= 50,blank=False,null= False)

    precio_producto = models.IntegerField('Precio Producto', blank= False, null=False)
    
    stock_producto = models.IntegerField('Stock del producto', blank= False, null= False, default=0)

    fecha_creacion = models.DateTimeField('Fecha de creación', auto_now=True)