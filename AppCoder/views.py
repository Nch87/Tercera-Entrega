from django.shortcuts import render
from .models import *
from django.http import HttpResponse
from .forms import ClienteForm, ProductoForm, ProveedorForm, VendedorForm


# Create your views here.

#def alta_cliente(request):
#    nombre_cliente="Ezequiel"
#   email_cliente="eze@gmail.com"
#    direccion_cliente="Calle Falsa 123"
#   print("Alta Cliente")
#    cliente= Cliente(nombre=nombre_cliente,=email_cliente,email=email_cliente,direccion=direccion_cliente)
#    cliente.save()
#    respuesta=f"Nuevo Cliente: {nombre_cliente} - {email_cliente}"
#    return HttpResponse(respuesta)

def inicio(request):
    return render(request,"AppCoder/inicio.html")

def cliente(request):
    if request.method=="POST":
        form=ClienteForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            nombre_cli=info["nombre"]
            apellido_cli=info["apellido"]
            dni_cli=info["dni"]
            telefono_cli=info["telefono"]
            email_cli=info["email"]
            direccion_cli=info["direccion"]
            cliente=Cliente(nombre=nombre_cli,apellido=apellido_cli,dni=dni_cli,email=email_cli,direccion=direccion_cli,telefono=telefono_cli)
            cliente.save()
            formulario_cliente=ClienteForm()
            return render(request,"AppCoder/cliente.html", {"mensaje":"Cliente Creado", "formulario": formulario_cliente})
        return render(request,"AppCoder/cliente.html", {"mensaje":"Datos Invalidos"})
    else:
        formulario_cliente=ClienteForm()
        return render(request,"AppCoder/cliente.html", {"formulario": formulario_cliente})
    
def producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            nombre=info["nombre"]
            descripcion = info["descripcion"]
            precio = info["precio"]
            producto=Producto(nombre=nombre,descripcion=descripcion,precio=precio)
            producto.save()
            formulario_producto=ProductoForm()
            return render(request,"AppCoder/productos.html", {"mensaje":"Producto Creado", "formulario": formulario_producto})
        return render(request,"AppCoder/productos.html", {"mensaje":"Datos Invalidos"})
    else:
        formulario_producto=ProductoForm()
        return render(request,"AppCoder/productos.html", {"formulario": formulario_producto}) 


def vendedor(request):
    if request.method == 'POST':
        form = VendedorForm (request.POST)
        if form.is_valid():
            info=form.cleaned_data
            nombre =info["nombre"]
            apellido = info["apellido"]
            telefono = info["telefono"] 
            legajo = info["legajo"]
            vendedor=Vendedor(nombre=nombre,apellido=apellido,telefono=telefono,legajo=legajo)
            vendedor.save()
            formulario_vendedor=VendedorForm()
            return render(request,"AppCoder/vendedores.html", {"mensaje":"Vendedor Creado", "formulario": formulario_vendedor})
        return render(request,"AppCoder/vendedores.html", {"mensaje":"Datos Invalidos"})
    else:
        formulario_vendedor=VendedorForm()
        return render(request,"AppCoder/vendedores.html", {"formulario": formulario_vendedor})  

def proveedor(request):
    if request.method == 'POST':
        form = ProveedorForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            nombre =info["nombre"]
            direccion = info["direccion"]
            telefono = info["telefono"]
            proveedor=Proveedores(nombre=nombre,direccion=direccion,telefono=telefono)
            proveedor.save()
            formulario_proveedor=ProveedorForm()
            return render(request,"AppCoder/proveedores.html", {"mensaje":"Proveedor Creado", "formulario": formulario_proveedor})
        return render(request,"AppCoder/proveedores.html", {"mensaje":"Datos Invalidos"})
    else:
        formulario_proveedor=ProveedorForm()
        return render(request,"AppCoder/proveedores.html", {"formulario": formulario_proveedor}) 

def busquedaClientes(request):
    return render(request,"AppCoder/busquedaClientes.html")

def buscar(request):
    dni=request.GET["dni"]
    if dni!="":
        cliente=Cliente.objects.filter(dni=dni)
        return render(request, "AppCoder/resultadoBusqueda.html",{"cliente":cliente})
    else:
        return render(request,"AppCoder/busquedaClientes.html", {"mensaje":"No se ingresaron Datos"})