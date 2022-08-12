from django.contrib import admin

# Register your models here.
from personas.models import Domicilio, Persona

admin.site.register(Persona) #registramos el modelo de la clase Persona
admin.site.register(Domicilio)