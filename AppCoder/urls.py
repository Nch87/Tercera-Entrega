from django.urls import path
from .views import *


urlpatterns = [
    path("alta_cliente/", alta_cliente),
    path("Clientes/", cliente, name="Registrate"),
    path("Productos/", producto, name="Productos"),
    path("Categoria/", categoria, name="Categoria"),
    path("Pedidos/", pedidos, name="Pedidos"),

]