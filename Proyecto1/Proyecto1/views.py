from datetime import datetime
from django.template import loader
from django.http import HttpResponse
from django.shortcuts import render
from django.template import Template, Context


def saludo(request):  # esta es una vista
    # aca se puede usar cargadores, lo mejor es usar eso
    nombre = "Ricardo"
    fecha = datetime.now()
    materias = ["is2", "distri", "compiladores"]
    #doc_externo = open('/home/rick/Desktop/djangopr/Proyecto1/plantillas/file.html')
    #tlt = Template(doc_externo.read())
    #doc_externo.close()
    #doc_externo=loader.get_template('file.html')
    #ctx = Context({"nombre_persona": nombre, "fecha_actual": fecha, "temas_varios": materias})
    #documento = tlt.reder(ctx) este no nos sirve cuando usamos el DIR de settings osea el loader
    #documento = doc_externo.render({"nombre_persona": nombre, "fecha_actual": fecha, "temas_varios": materias})
    #return HttpResponse(documento)
    return render(request,"file.html",{"nombre_persona": nombre, "fecha_actual": fecha, "temas_varios": materias})

def servicios(request):
    fecha_actual=datetime.now()
    return render(request, "servicios.html",{"fecha": fecha_actual})
def contactos(request):
    nombre="Ricardo Jesus"
    return render(request, "contactos.html",{"fecha_persona": nombre})