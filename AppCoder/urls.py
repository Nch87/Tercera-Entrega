from django.urls import path
from .views import *


urlpatterns = [
    path("cliente/", cliente, name="cliente"),
    path("Productos/", producto, name="Productos"),
    path("Proveedores/", proveedor, name="Proveedores"),
    path("Vendedores/", vendedor, name="Vendedores"),
    path("busquedaClientes/", busquedaClientes, name="busquedaClientes"),
    path("buscar/", buscar, name="buscar"),
]