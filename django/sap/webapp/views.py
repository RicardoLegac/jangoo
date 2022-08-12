from django.http import HttpResponse
from django.shortcuts import render

from personas.models import Persona

# Create your views here.
def bienvenido(request):
    personas = Persona.objects.all()
    return render(request,'bienvenido.html',{'personas':personas})

def despedida(request):
    return HttpResponse('despedida xd')