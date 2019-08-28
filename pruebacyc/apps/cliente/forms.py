from django import forms
from .models import FichaCliente,Canal

class formCliente(forms.ModelForm):
    class Meta:
        model = FichaCliente
        fields = [
            'rut',
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
            'pNombre' : 'Primer nombre',
            'sNombre' : 'Segundo nombre',
            'apPaterno': 'Apellido paterno',
            'apMaterno' : 'Apellido materno',
            'direccion' : 'Dirección',
            'fNacimiento': 'Fecha de nacimiento',
            'email' : 'E-Mail(USUARIO)',
            'telefono' : 'Telefono',
        }
        widgets = {
            'rut': forms.TextInput(attrs={'class': 'form-control col-12 mb-3 justify-content-center'}),
            'pNombre' : forms.TextInput(attrs={'class': 'form-control col-12 mb-3 justify-content-center'}),
            'sNombre' : forms.TextInput(attrs={'class': 'form-control col-12 mb-3 justify-content-center'}),
            'apPaterno': forms.TextInput(attrs={'class': 'form-control col-12 mb-3 justify-content-center'}),
            'apMaterno' : forms.TextInput(attrs={'class': 'form-control col-12 mb-3 justify-content-center'}),
            'direccion' : forms.TextInput(attrs={'class': 'form-control col-12 mb-3 justify-content-center'}),
            'fNacimiento': forms.TextInput(attrs={'class': 'form-control col-12 mb-3 justify-content-center','type':'date'}),
            'email' : forms.TextInput(attrs={'class': 'form-control col-12 mb-3 justify-content-center','type': 'email'}),
            'telefono': forms.TextInput(attrs={'class':'form-control col-12 mb-3 justify-content-center'}),
        }
    def clean(self):
        cleaned_data = super().clean()
        Rut = cleaned_data.get("rut")
        validaRut = FichaCliente.objects.filter(rut=Rut).exists()
        pNombre = cleaned_data.get("pNombre")
        if not len(Rut) == 9 :
                raise forms.ValidationError(
                    "El numero tiene que ser igual a 9"
                )
        if len(pNombre) <= 1:
            raise forms.ValidationError(
                "Debe ingresar un primer nombre"
            )
        if validaRut:
            raise forms.ValidationError(
                "El rut ingresado ya existe"
            )
class formCanal(forms.ModelForm):
    class Meta:
        model = Canal
        fields = [
            'tipoCanal',
        ]
        labels = {
            'tipoCanal': 'Tipo de canal',
        }
        widgets = {
            'tipoCanal': forms.Select(attrs={'class': 'form-control col-12 mb-3 justify-content-center'}),
        }
