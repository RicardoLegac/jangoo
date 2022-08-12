from tkinter import Widget
from personas.models import Persona
from django.forms import ModelForm, EmailInput
class personaForm(ModelForm):
    class Meta:
        model = Persona
        fields = '__all__'
        widgets = {
            'email': EmailInput(attrs={'type': 'email'}) #validacion para que ingrese un email

        }

