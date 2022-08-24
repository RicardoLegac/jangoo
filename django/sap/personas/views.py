import re
from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect
from django.forms import modelform_factory,inlineformset_factory
from personas.forms import personaForm
from personas.models import Persona
# Create your views here.
def detallePersona(request,id):
    #persona = Persona.objects.get(pk=id)
    #en vez de usar get podemos usar la siguiente sintaxis
    persona = get_object_or_404(Persona, pk=id)
    #esto es para que no salte error al llamar un id que no existe
    return render(request, 'persona/detalle.html',{'p':persona})

#PersonaForm = modelform_factory(Persona,exclude=[])
#personaform= inlineformset_factory(Persona, fields =['id', 'name','apellido','email'])
def nuevaPersona(request):
    if request.method == 'POST':
        formaPersona = personaForm(request.POST)
        if formaPersona.is_valid():
            formaPersona.save()
            return redirect('index')
        else:
            return render(request, 'persona/nuevo.html',{'formapersona':persona})
    else:
        persona = personaForm()
        return render(request, 'persona/nuevo.html',{'formapersona':persona})

def editarPersona(request,id):
    persona = get_object_or_404(Persona,pk=id)
    if request.method=='POST':
        formaPersona = personaForm(request.POST,instance = persona)
        if formaPersona.is_valid():
            formaPersona.save()
            return redirect('index')
    else: 
       
        formaPersona = personaForm(instance=persona)
    return render(request,'persona/editar.html',{'formaPersona':formaPersona})

def eliminarPersona(request,id):
    persona = get_object_or_404(Persona, pk=id) #recuperamos la persona de la base de datos segun el id que hayamos seleccionado
    if persona: #si existe el registro persona
        persona.delete()
    return redirect('index')