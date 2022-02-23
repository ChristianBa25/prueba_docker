from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from gestionProductos.utils.mongo import MongoConnection
from bson.objectid import ObjectId

# Create your views here.
def inicio(request):
    producto_anadido = False
    try:
        
        documento = {}
        nombreProducto = request.GET["nombre"]
        descripionProducto = request.GET["descripcion"]
        cantidadProducto = int(request.GET["cantidad"])
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

        
        agregarABaseDatos(documento)
        producto_anadido = True
    except:
        producto_anadido = False
    
    return render(request, "composeexample/index.html", {"producto_anadido": producto_anadido})

def agregarABaseDatos(documento):
    agregar = MongoConnection()
    agregar.insert_document(documento)

    

def productos(request, llamada=False):
    busqueda = MongoConnection()
    a = busqueda.find_all_documents()
    response=[]
    coleccion=[]
    for i in a:
        coleccion.append(i)
        response.append(i["_id"])
    
    if llamada:
        return coleccion
    return render(request, "composeexample/lista_productos.html", {"busqueda":response,"coleccion":coleccion})


def buscar(request):
    comando = {}
    try:
        categoria = request.GET["categoria_buscar"]
    except:
        pass
    try:
        condicional = request.GET["condicional_buscar"]
        descripcion = request.GET["descripcion_buscar"]
    
        if condicional == "1":
            condicional = "$eq"
            comando[categoria]= {condicional: int(descripcion)}
        elif condicional == "2":
            condicional = "$gt"
            comando[categoria]= {condicional: int(descripcion)}
        elif condicional == "3":
            condicional = "$gte"
            comando[categoria]= {condicional: int(descripcion)}
        elif condicional == "4":
            condicional = "$lte"
            comando[categoria]= {condicional: int(descripcion)}
        elif condicional == "5":
            condicional = "$ne"
            comando[categoria]= {condicional: int(descripcion)}
        elif condicional == "6":
            comando[categoria] = descripcion
        elif condicional == "7":
            comando['_id'] = ObjectId(descripcion)
        elif condicional == "8":
            documentos= productos(request, True)
            response= []

            for documento in documentos:
                for key,value in documento.items():
                    if value == descripcion:
                        response.append(documento)
            

        if condicional != "8":    
            busqueda = MongoConnection()
            a = busqueda.find_specific_documents(comando)


            response=[]
            id_mostrados=[]
            for i in a:
                
                id_mostrados.append(i['_id'])
                response.append(i)
            #id_mostrados = id_mostrados[0]
        
    except:
        id_mostrados={}
        response="No se ha encontrado nada, realiza una busqueda"
    return render(request, "composeexample/buscar.html", {"resultado": response})

def borrar(request):
    comando = {}
    try:
        id_mostrados = request.GET["dato_a_borrar"]
        comando['_id'] = ObjectId(id_mostrados)

        

    except:
        comando["delete"] = "Not found"

    borrar = MongoConnection()
    borrar.delete_documents(comando)
    

    
    return render(request, "composeexample/delete.html", {})