from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def bienvenido(request):
    return HttpResponse('return views')

def despedida(request):
    return HttpResponse('despedida xd')