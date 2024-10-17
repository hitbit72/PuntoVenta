from django.db import models

# Campos de nuestra base de datos

# AutoField,primary_key = True si no desea utilizar el campo
# predeterminado "id" proporcionado por django

class Cliente(models.Model):
    #id = models.AutoField(primary_key=True)
    codigo = models.CharField(max_length=50, unique=True, null=True, blank=True)
    nombre = models.CharField(max_length=200, unique=True, null=False, blank=False)
    telefono = models.CharField(max_length=20, unique=False, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'clientes'
        verbose_name_plural = 'clientes'

    def __str__(self):
        return self.nombre
    

class Producto(models.Model):
    #id = models.AutoField(primary_key=True)
    codigo = models.CharField(max_length=255, unique=True, null=False, blank=False)
    descripcion = models.CharField(max_length=255, unique=True, null=False, blank=False)
    imagen = models.ImageField(upload_to='productos', null=True, blank=True)
    costo = models.DecimalField(max_digits=15, decimal_places=2, null=False)
    cantidad = models.DecimalField(max_digits=15, decimal_places=2, null=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'producto'
        verbose_name_plural = 'productos'
        order_with_respect_to = 'descripcion'

    def __str__(self):
        return self.descripcion
    