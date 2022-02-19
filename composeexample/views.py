from xml.dom.minidom import Document
from django.http import HttpResponse
from django.template import Template, Context
from django.template.loader import get_template
from django.shortcuts import render

def saludo(request):
    nombre = "Juan"
    apellido = "Gomez"

    # doc_externo = open("C:/Users/Christian/Documents/Django_pruebas/prueba1/prueba1/templates/plantilla1.html")
    # plt = Template(doc_externo.read())
    # doc_externo.close()
    # ctx = Context({"nombre_persona" : nombre, "apellido_persona" : apellido})
    # documento = plt.render(ctx)

    # En caso de no usar las lineas comentadas para usar un cargador o loader se usa así antes
    # poniendo la ruta en settings.py en Templates y Dir[]:

    #doc_externo = get_template('plantilla1.html')

    # documento = doc_externo.render({"nombre_persona" : nombre, "apellido_persona" : apellido})

    return render(request, "composeexample/plantilla1.html", {"nombre_persona" : nombre, "apellido_persona" : apellido})


