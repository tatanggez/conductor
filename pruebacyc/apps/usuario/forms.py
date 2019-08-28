from django import forms
from .models import FichaUsuario,Contrato


class formUsuario(forms.ModelForm):
    class Meta:
        model = FichaUsuario
        fields = [
            'rut',
            'dv',
            'pNombre',
            'sNombre',
            'apPaterno',
            'apMaterno',
            'direccion',
            'fNacimiento',
            'email',
            'telefono',
        ]
        labels = {
            'rut': 'Rut',
            'dv': 'Dv',
            'pNombre' : 'Primer nombre',
            'sNombre' : 'Segundo nombre',
            'apPaterno': 'Apellido paterno',
            'apMaterno' : 'Apellido materno',
        }
        widgets = {
            'rut': forms.TextInput(attrs={'class': 'form-control col-12 mb-3 justify-content-center'}),
            'dv': forms.TextInput(attrs={'class': 'form-control col-12 mb-3 justify-content-center'}),
            'pNombre' : forms.TextInput(attrs={'class': 'form-control col-12 mb-3 justify-content-center'}),
            'sNombre' : forms.TextInput(attrs={'class': 'form-control col-12 mb-3 justify-content-center'}),
            'apPaterno': forms.TextInput(attrs={'class': 'form-control col-12 mb-3 justify-content-center'}),
            'apMaterno' : forms.TextInput(attrs={'class': 'form-control col-12 mb-3 justify-content-center'}),
        }

class formContrato(forms.ModelForm):
    class Meta:
        model = Canal
        fields = [
            'tipoContrato',
        ]
        labels = {
            'tipoContrato': 'Tipo de contrato',
        }
        widgets = {
            'tipoContrato': forms.Select(attrs={'class': 'form-control col-12 mb-3 justify-content-center'}),
        }