from django import forms


class ClienteForm(forms.Form):
    nombre = forms.CharField(max_length=100)
    apellido = forms.CharField(max_length=100)
    dni = forms.CharField(max_length=10)
    telefono = forms.CharField(max_length=20)
    email = forms.EmailField()
    direccion = forms.CharField(max_length=200)
    

class ProductoForm(forms.Form):
    nombre = forms.CharField(max_length=100)
    descripcion = forms.CharField(widget=forms.Textarea)
    precio = forms.DecimalField(decimal_places=2)
    

class ProveedorForm(forms.Form):
    nombre = forms.CharField(max_length=100)
    direccion = forms.CharField(max_length=200)
    telefono = forms.CharField(max_length=20)


class VendedorForm(forms.Form):
    nombre = forms.CharField(max_length=100)
    apellido = forms.CharField(max_length=200)
    telefono = forms.CharField(max_length=20)
    legajo = forms.CharField(max_length=10)
