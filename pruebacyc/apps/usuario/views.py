from django.shortcuts import render

# Create your views here.
from .models import FichaUsuario,Contrato
from .forms import formUsuario,formContrato

from django.contrib.auth.forms import UserCreationForm

def registrarUsuario(request):
    if request.method == "POST":
        form_usuario = formUsuario(request.POST)
        form_contrato = formContrato(request.POST)
        if form_contrato.is_valid() and form_usuario.is_valid():
            contratos = form_contrato.save()
            usuario = form_usuario.save(commit=False)
            usuario.contrato=contratos
            usuario.save()
            #return redirect('admin')
    else:
        form_usuario = formUsuario()
        form_contrato = formContrato() 
    args = {}
    args['form_usuario'] = form_usuario
    args['form_contrato'] = form_contrato

    return render(request,"cliente/fichacliente.html",args)