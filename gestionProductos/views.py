from django.shortcuts import render
from django.http import HttpResponse
from gestionProductos.models import Articulos

# Create your views here.
def inicio(request):
    
    return render(request, "composeexample/index.html", {})

def agregarABaseDatos(documento):
    # articulos = Articulos.producto
    # articulo_id = articulos.insert_one(documento).inserted_id
    # articulo_id
    pass

def productos(request):
    documento = {}
    nombreProducto = request.GET["nombre"]
    descripionProducto = request.GET["descripcion"]
    cantidadProducto = request.GET["cantidad"]
    estadoProducto = request.GET["activo"]

    #Añadir datos en diccionario
    if nombreProducto != "":
        documento["Nombre"] = nombreProducto
    
    if descripionProducto != "":
        documento["Descripcion"] = descripionProducto
    
    if cantidadProducto:
        documento["Cantidad"] = cantidadProducto

    if estadoProducto == 1:
        documento["Estado"] = "Activo"
    else:
        documento["Estado"] = "Desactivado"
    

    # Recibir datos de inputs dinámicos
    keys = []
    values = []
    numeroInputs = 1
    
    while True:
        try:
            nombreInputDinamico = "key"+str(numeroInputs)
            descripcionInputDinamico = "value"+str(numeroInputs)
            
            if request.GET[nombreInputDinamico]:
                
                keys.append(request.GET[nombreInputDinamico])
                values.append(request.GET[descripcionInputDinamico])
            
            numeroInputs+=1
        except:
            break

    #Añadir inputs dinámicos a diccionario

    if keys:
        indice = 0
        for i in keys:
            documento[i] = values[indice]
            indice += 1

    mensaje = (documento)
     
    agregarABaseDatos(documento)

    return HttpResponse(mensaje)