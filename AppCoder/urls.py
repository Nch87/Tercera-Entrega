from django.urls import path
from .views import *


urlpatterns = [
    path("alta_cliente/", alta_cliente),
    path("cliente/", cliente, name="cliente"),
    path("Productos/", producto, name="Productos"),
    path("Proveedores/", proveedor, name="Proveedores"),
    path("Vendedores/", vendedor, name="Vendedores"),
    path("busquedaClientes/", busquedaClientes, name="busquedaClientes")
]