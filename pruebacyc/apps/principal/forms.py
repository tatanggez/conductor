from django import forms
from .models import Ubicacion,UbicacionFinal

class UbicacionForm(forms.ModelForm):
    class Meta:
        model = Ubicacion
        fields = '__all__'

class UbicacionFinalForm(forms.ModelForm):
    class Meta:
        model = UbicacionFinal
        fields = '__all__'
