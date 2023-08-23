from django.db import models

# Create your models here.

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    direccion = models.TextField()

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

class Pedido(models.Model):
    fecha = models.DateField()
    productos = models.ManyToManyField(Producto)
    total = models.DecimalField(max_digits=8, decimal_places=2)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
