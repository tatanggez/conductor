from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect
from django.contrib import messages
from apps.conductor.models import FichaConductor
from django.contrib.auth.decorators import login_required
from apps.conductor.forms import formConductor2
 
import json
 
from django.template import RequestContext
from django.utils.timesince import timesince
from .models import Ubicacion
from .forms import UbicacionForm, UbicacionFinalForm
# Create your views here.


@login_required
def menu(request):
    us = request.user
    Conductor = FichaConductor.objects.filter(Usuario_id=us.id)
    return render(request,'Menu/principal.html',{'Conductor':Conductor})

@login_required
def mapa(request):
    form = UbicacionForm()
    return  render(request,'Menu/mapa.html', {'form':form})

@login_required
def editarPerfil(request,user_id):
    Conductor = FichaConductor.objects.get(Usuario_id = user_id)
    if request.method == 'GET':
        form = formConductor2(instance=Conductor)
    else:
        form = formConductor2(request.POST, instance=Conductor)
        if form.is_valid():
            form.save()
        return redirect('principal:menu')
    return  render(request,'Menu/editarPerfil.html',{'form':form})

@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('index')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'registration/cambiaPass.html', {
        'form': form
    })

def index(request):
    form = UbicacionForm()
    ubicaciones = Ubicacion.objects.all().order_by('fecha')
 
    return render('mapa.html', {'form':form,'ubicaciones':ubicaciones}, RequestContext(request))


def index2(request):
    form = UbicacionFinalForm()

    return render(request,'Menu/mapa2.html', {'form':form}, RequestContext(request))
 
def coords_obtener(request):
 
    ubicacion = Ubicacion.objects.get(id=request.POST['value'])
 
    return HttpResponse(json.dumps({'lat': ubicacion.lat, 'lng':ubicacion.lng}))
 
 
 
def coords_eliminar(request):
 
    #obtenemos la id de ubicacion
    id = request.POST['value']
 
    #eliminamos la ubicacion
    Ubicacion.objects.filter(id=id).delete()
 
    #obtenemos todos los objetos en un html
    data = getHTML()
 
    #retornamos la respuesta para mostrarlo
    return HttpResponse(json.dumps({'ok': True, 'msg': data}))
 
 
#metodo para obtener el html que lista los objetos

 
 
def coords_save(request):
 
    if request.is_ajax():
 
        formUb = UbicacionForm(request.POST)
 
        if formUb.is_valid():
 
            formUb.save()
            
 
            return HttpResponse(json.dumps({'ok': True, 'msg': 'Ok'}))
        else:
            return HttpResponse(json.dumps({'ok': False, 'msg': 'Debes llenar todos los campos'}))


 
def coords_save(request):
 
    if request.is_ajax():
 
        formUb = UbicacionForm(request.POST)
 
        if formUb.is_valid():
 
            formUb.save()
            
 
            return HttpResponse(json.dumps({'ok': True, 'msg': 'Ok'}))
        else:
            return HttpResponse(json.dumps({'ok': False, 'msg': 'Debes llenar todos los campos'}))


def coords_save2(request):
 
    if request.is_ajax():
 
        formUb = UbicacionFinalForm(request.POST)
 
        if formUb.is_valid():
 
            formUb.save()
            
 
            return HttpResponse(json.dumps({'ok': True, 'msg': 'Ok'}))
        else:
            return HttpResponse(json.dumps({'ok': False, 'msg': 'Debes llenar todos los campos'}))