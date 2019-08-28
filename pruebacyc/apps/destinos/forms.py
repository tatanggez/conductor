from django import forms
from .models import Comuna

class Comuna(forms.ModelForm):
    class Meta:
        model = Comuna
        fields = [
            'Comuna',
            'Direccion',
        ]
        labels = {
            'Comuna': 'Comuna',
            'Direccion': 'Dirección',
        }
        widgets = {
            'Comuna': forms.Select(attrs={'class': 'form-control col-12 mb-3 justify-content-center'}),
            'Direccion' : forms.TextInput(attrs={'class': 'form-control col-12 mb-3 justify-content-center'}),
        }

