from django import forms
from .models import Tarea

class TareasForm(forms.ModelForm):
    class Meta:
        model = Tarea
        fields = ['titulo','descripcion', 'importante']
        widgets = {
            'titulo': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Escribe el titulo de la tarea'}),
            'descripcion': forms.Textarea(attrs={'class':'form-control','placeholder':'Escribe la descripcion de la tarea'}),
            'importante': forms.CheckboxInput(attrs={'class':'form-check-input m-auto'}),
        }
        