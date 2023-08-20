from django.http import HttpResponse
from django.template import Template, Context 

def saludar(request):
    return HttpResponse("Hola Mundo")
    
def saludo_con_nombre(request, nombre):
    return HttpResponse(f"<h1> Hola {nombre} <h1>")

def probandohtml(request):
    #creamos un diccionario vacio
    diccionario={} 
    #abrimos el archivo de plantillas
    archivo = open(r"C:\Users\Natalia\Desktop\Entregable_3\Proyecto3\plantillas\template1.html") 
    contenido = archivo.read() #leemos el contenido del archivo con READ
    archivo.close() #cerramos el archivo que estabamos leyendo con CLOSE
    template = Template(contenido) #creamos el Template con la clase django
    contexto = Context(diccionario) #creamos el contexto 
    documento= template.render(contexto) #modificamos el template con los datos del contexto
    return HttpResponse(documento) 