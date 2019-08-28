from django.shortcuts import render,redirect
from django.http import HttpResponse
# Create your views here.

from .models import FichaCliente,Canal
from .forms import formCliente,formCanal


# Create your views here.
def registrarCliente(request):
    if request.method == "POST":
        form_cliente = formCliente(request.POST)
        form_canal = formCanal(request.POST)
        if form_canal.is_valid() and form_cliente.is_valid():
            canal = form_canal.save()
            cliente = form_cliente.save(commit=False)
            cliente.Centro=canal
            cliente.save()
            #return redirect('admin')
    else:
        form_cliente = formCliente()
        form_canal = formCanal() 
    args = {}
    args['form_cliente'] = form_cliente
    args['form_canal'] = form_canal

    return render(request,"cliente/fichacliente.html",args)