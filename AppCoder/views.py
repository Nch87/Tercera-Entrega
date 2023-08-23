from django.shortcuts import render
from .models import Cliente
from django.http import HttpResponse

# Create your views here.

def alta_cliente(request):

    nombre_cliente="Ezequiel"
    email_cliente="eze@gmail.com"
    direccion_cliente="Calle Falsa 123"
    print("Alta Cliente")
    cliente= Cliente(nombre=nombre_cliente,email=email_cliente,direccion=direccion_cliente)
    cliente.save()
    respuesta=f"Nuevo Cliente: {nombre_cliente} - {email_cliente}"
    return HttpResponse(respuesta)

def inicio(request):
    return render(request,"AppCoder/inicio.html")

def cliente(request):
    return render(request,"AppCoder/cliente.html")

def producto(request):
    return render(request,"AppCoder/productos.html")

def categoria(request):
    return render(request,"AppCoder/categoria.html")

def pedidos(request):
    return render(request,"AppCoder/pedidos.html")