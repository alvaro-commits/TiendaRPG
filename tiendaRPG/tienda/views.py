from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import models as mod
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView
from datetime import datetime
from django.db.models import Avg, Max, Min, Sum,F





@login_required
def Vistacarro(request):
    contexto = {}
    carro_qs = mod.carro.objects.filter(usuario=request.user, realizado=False)
    if carro_qs.exists():
        carro = mod.carro.objects.get(usuario=request.user, realizado=False)
        contexto = {
            'carro' : carro,
            'itemscarro' : carro.items}
        acumulacionTotal = 0
        acumulacionPuntos = 0
        for p in carro.items.all():
           precio = p.producto.precio 
           puntos = p.producto.puntos
           acumulacionTotal = acumulacionTotal + precio
           acumulacionPuntos = acumulacionPuntos + puntos
           carro.preciototal = acumulacionTotal
           carro.totalpuntos = acumulacionPuntos
           carro.save()
    return render(request,'carro.html', contexto)

@login_required
def realizarcompra(request):
    carro_qs = mod.carro.objects.filter(usuario=request.user, realizado=False)
    if carro_qs.exists():
        carro = mod.carro.objects.get(usuario=request.user, realizado=False)
        carro.realizado = True 
        carro.fechaVenta = datetime.now()
        carro.save()
        perfil_qs = mod.Perfil.objects.filter(usuario=request.user)
        if perfil_qs.exists():
            perfil = mod.Perfil.objects.get(usuario=request.user)
            perfil.total_puntos = perfil.total_puntos + carro.totalpuntos
            perfil.save()
        else:
            Nuevoperfil = mod.Perfil.objects.create(usuario=request.user, total_puntos = carro.totalpuntos)
        contexto = {
            'carro' : carro}
        return render(request,'boleta.html', contexto)
    else:
        return redirect('/')


@login_required
def seleccionPersonaje(request):
    clase = mod.Clase_Personaje.objects.all()
    perfil_qs = mod.Perfil.objects.filter(usuario=request.user,clase= None )
    if perfil_qs.exists():
        perfil = mod.Perfil.objects.get(usuario=request.user,clase= None )
        contexto = {
           'clases' : clase,
            'perfil' : perfil
        }
        return render(request,'seleccionPersonaje.html', contexto)
    else:
        return redirect('/perfil')


@login_required
def asignarClaseAPersonaje(request,**kwargs):
    Perfil = mod.Perfil.objects.get(usuario = request.user )
    clase = mod.Clase_Personaje.objects.get(id = kwargs.get('id',""))
    accesorios = mod.Accesorio.objects.filter(tier='0')
    for ac in accesorios:
        perfil_accesorio = mod.Perfil_Accesorio.objects.create(accesorio = ac)
        Perfil.accesorios.add(perfil_accesorio)
    Perfil.clase = clase
    Perfil.save()
    return redirect('/perfil')

@login_required
def vistaperfil(request):
    perfil = mod.Perfil.objects.get(usuario = request.user)
    boamano = perfil.accesorios
    accesorio_perfil = perfil.accesorios.all()
    for accesorio in accesorio_perfil:
        pass
    ace = mod.Accesorio.objects.filter(tipoAccesorio = "ca").aggregate(Max('tier')).get('tier__max')
    ak = mod.Accesorio.objects.filter(tipoAccesorio = "ca", tier = ace)
    a = 1

    for ac in accesorio_perfil:
        casco_equipado = ac.accesorio
        peto_equipado = ac.accesorio
        manoplas_equipas = ac.accesorio
        pantalones_equipados = ac.accesorio
        grebas_equipadas = ac.accesorio
        anillo_equipado = ac.accesorio
    if perfil.derrotas == 0:
        kda = perfil.victorias 
    else:
        kda = perfil.victorias / perfil.derrotas
    contexto = {
        'perfil' : perfil,
        'accesorio_equipado' : perfil.accesorios,
        'kda': kda
    }
    return render(request,'perfil.html',contexto)


def login(request):

    return render(request,'Login.html')


def registro(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Tu cuenta ha sido creada exitosamente! ahora puedes ingresar.')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request,'registro.html',{'form': form})

class VistaMenu(ListView):
    model = mod.Productos
    template_name = "index.html"

def añadir_al_carro(request,**kwargs):
    if request.user.is_authenticated:
        producto= mod.Productos.objects.filter(codigo_producto=kwargs.get('codigo_producto',"")).first()
        item_carro = mod.CarroProducto.objects.create(producto = producto)
        carro_qs = mod.carro.objects.filter(usuario=request.user, realizado=False)
        if carro_qs.exists():
            carro = mod.carro.objects.get(usuario=request.user, realizado=False)
            carro.items.add(item_carro)
            carro.save()
        else:
            carro = mod.carro.objects.create(usuario=request.user)
            carro.items.add(item_carro)
            carro.save()
        return redirect('/carro')
    else:
        return redirect('/registro')

def eliminar_item_carro(request,**kwargs):   
    producto_a_eliminar = mod.CarroProducto.objects.get(pk=kwargs.get('item_id',""))
    producto_a_eliminar.delete()
    return redirect('/carro')