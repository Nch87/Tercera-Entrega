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


