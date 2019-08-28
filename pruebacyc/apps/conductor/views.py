from django.shortcuts import render,redirect
from django.http import HttpResponse
# Create your views here.

from .models import FichaConductor,Tvehiculo, Tlicencia
from .forms import formConductor,formVehiculo,formLicencia
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
def registrarCuenta(request):
    if request.method == "POST":
        form_conductor = formConductor(request.POST)
        form_licencia = formLicencia(request.POST)
        form_vehiculo = formVehiculo(request.POST)
        form = UserCreationForm(request.POST)
        if form_vehiculo.is_valid() and form_conductor.is_valid() and form.is_valid() and form_licencia.is_valid():
            vehiculo = form_vehiculo.save()
            conductor = form_conductor.save(commit=False)
            user = form.save()
            licencia = form_licencia.save()
            conductor.licencia=licencia
            conductor.Vehiculo=vehiculo
            conductor.Usuario=user
            conductor.save()
            #return redirect('login')
    else:
        form_conductor = formConductor()
        form_licencia = formLicencia()
        form_vehiculo = formVehiculo() 
        form = UserCreationForm()
    args = {}
    args['form_conductor'] = form_conductor
    args['form_licencia'] = form_licencia
    args['form_vehiculo'] = form_vehiculo
    args['form_Reg'] = form

    return render(request,"conductor/fichaconductor.html",args)
