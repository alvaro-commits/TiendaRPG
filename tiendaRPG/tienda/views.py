from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import models as mod
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.models import User
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
    perfil_qs = mod.Perfil.objects.filter(usuario = request.user)
    if(not perfil_qs.exists()):
        mod.Perfil.objects.create(usuario=request.user)
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
    for accesorio_inicial in accesorios:
        Perfil.accesorios.add(accesorio_inicial)
    Perfil.clase = clase
    Perfil.save()
    return redirect('/perfil')

@login_required
def vistaperfil(request):
    perfil_qs = mod.Perfil.objects.filter(usuario = request.user)
    if(not perfil_qs.exists()):
        return redirect('/seleccionPersonaje')
    perfil = mod.Perfil.objects.get(usuario = request.user)
    clasePerfil = perfil.clase
    if clasePerfil != None:
        cascos = mod.Accesorio.objects.filter(tipoAccesorio = "ca")[1:]
        petos = mod.Accesorio.objects.filter(tipoAccesorio = "pe")[1:]
        manoplas = mod.Accesorio.objects.filter(tipoAccesorio = "ma")[1:]
        pantalones = mod.Accesorio.objects.filter(tipoAccesorio = "pa")[1:]
        grebas = mod.Accesorio.objects.filter(tipoAccesorio = "gr")[1:]
        anillos = mod.Accesorio.objects.filter(tipoAccesorio = "an")[1:]

        maxTierCasco = perfil.accesorios.filter(tipoAccesorio = "ca").aggregate(Max('tier')).get('tier__max')
        maxTierPeto = perfil.accesorios.filter(tipoAccesorio = "pe").aggregate(Max('tier')).get('tier__max')
        maxTierManop = perfil.accesorios.filter(tipoAccesorio = "ma").aggregate(Max('tier')).get('tier__max')
        maxTierPant = perfil.accesorios.filter(tipoAccesorio = "pa").aggregate(Max('tier')).get('tier__max')
        maxTierGreb = perfil.accesorios.filter(tipoAccesorio = "gr").aggregate(Max('tier')).get('tier__max')
        maxTierAnil = perfil.accesorios.filter(tipoAccesorio = "an").aggregate(Max('tier')).get('tier__max')

        casco_equipado = perfil.accesorios.get(tier = maxTierCasco, tipoAccesorio = "ca")
        peto_equipado = perfil.accesorios.get(tier = maxTierPeto, tipoAccesorio = "pe")
        manoplas_equipadas = perfil.accesorios.get(tier = maxTierManop, tipoAccesorio = "ma")
        pantalones_equipadas = perfil.accesorios.get(tier = maxTierPant, tipoAccesorio = "pa")
        grebas_equipadas = perfil.accesorios.get(tier = maxTierGreb, tipoAccesorio = "gr")
        anillo_equipado = perfil.accesorios.get(tier = maxTierAnil, tipoAccesorio = "an")

        clase = perfil.clase
        vida_base =clase.vida_base
        daño_base =clase.daño_base
        defensa_base =clase.defensa_base

        vida_total = vida_base + casco_equipado.vida_extra + peto_equipado.vida_extra + manoplas_equipadas.vida_extra + pantalones_equipadas.vida_extra + grebas_equipadas.vida_extra + anillo_equipado.vida_extra
        perfil.vida_total = vida_total

        daño_total = daño_base + casco_equipado.daño_extra + peto_equipado.daño_extra + manoplas_equipadas.daño_extra + pantalones_equipadas.daño_extra + grebas_equipadas.daño_extra + anillo_equipado.daño_extra
        perfil.daño_total = daño_total

        defensa_total = defensa_base + casco_equipado.defensa_extra + peto_equipado.defensa_extra + manoplas_equipadas.defensa_extra + pantalones_equipadas.defensa_extra + grebas_equipadas.defensa_extra + anillo_equipado.defensa_extra
        perfil.defensa_total = defensa_total

        posionesVida = mod.PosionPerfil.objects.filter(perfil = perfil, posion__nombre ='pócima de vida' ).count()
        posionesDaño = mod.PosionPerfil.objects.filter(perfil = perfil, posion__nombre ='pócima de daño' ).count()
        posion = mod.Posion.objects.all()
        
        perfil.save()
        if perfil.derrotas == 0:
            kda = perfil.victorias 
        else:
            kda = perfil.victorias / perfil.derrotas
        contexto = {
            'posionesTotalesVida': posionesVida,
            'posionesTotalesDaño': posionesDaño,
            'perfil' : perfil,
            'casco_equipado' : casco_equipado,
            'peto_equipado' : peto_equipado,
            'manoplas_equipadas' : manoplas_equipadas,
            'pantalones_equipados' : pantalones_equipadas,
            'grebas_equipadas' : grebas_equipadas,
            'anillo_equipado' : anillo_equipado,
            'cascos' : cascos,
            'petos' : petos,
            'manoplas' : manoplas,
            'pantalones' : pantalones,
            'grebas' : grebas,
            'anillos' : anillos,
            'kda': kda,
            'posiones': posion
        }
        return render(request,'perfil.html',contexto)
    else:
       return redirect('/seleccionPersonaje') 



def comprarAccesorio(request,**kwargs):
    perfil = mod.Perfil.objects.get(usuario = request.user)
    accesorio = mod.Accesorio.objects.get(id = kwargs.get('accesorio_id'))
    if(perfil.total_puntos >= accesorio.costo_puntos):
        perfil.accesorios.add(accesorio)
        perfil.total_puntos = perfil.total_puntos - accesorio.costo_puntos
        perfil.save()
        messages.success(request, 'Tu compra ha sido realizada exitosamente!')
    else:
        messages.warning(request, 'No tienes los puntos suficientes.')
    return redirect('/perfil')

def comprarPosion(request,**kwargs):
    perfil = mod.Perfil.objects.get(usuario = request.user)
    posion = mod.Posion.objects.get(id = kwargs.get('posion_id'))
    ordenPosion = mod.PosionPerfil.objects.create(posion = posion)
    perfil.save()
    posionesVida = mod.PosionPerfil.objects.filter(perfil = perfil, posion__nombre ='pócima de vida' ).count()
    posionesDaño = mod.PosionPerfil.objects.filter(perfil = perfil, posion__nombre ='pócima de daño' ).count()
    if(perfil.total_puntos >= posion.costo):
        if(posionesVida <3 and posion.nombre == "pócima de vida" ):
            perfil.posion.add(ordenPosion)
            perfil.total_puntos = perfil.total_puntos - posion.costo
            perfil.save()
            messages.success(request, 'Tu compra ha sido realizada exitosamente!')   
        elif(posion.nombre == "pócima de vida"):
            messages.warning(request, 'Ya tienes el maximo de posiones de vida.')
        if(posionesDaño <3 and posion.nombre == "pócima de daño"):
            perfil.posion.add(ordenPosion)
            perfil.total_puntos = perfil.total_puntos - posion.costo
            perfil.save()
            messages.success(request, 'Tu compra ha sido realizada exitosamente!')
        elif(posion.nombre == "pócima de daño"):
            messages.warning(request, 'Ya tienes el maximo de posiones de daño.')
    else:
        messages.warning(request, 'No tienes los puntos suficientes.')
    return redirect('/perfil')

def login(request):

    return render(request,'Login.html')


def registro(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            nombre = form.cleaned_data.get('username')
            usuario = User.objects.get(username = nombre)
            mod.Perfil.objects.create(usuario = usuario)
            messages.success(request, f'Tu cuenta ha sido creada exitosamente! ahora puedes ingresar.')
            return redirect('login')
        else:
            messages.warning(request, f'El nombre de usuario ingresado ya se encuentra registrado.')
            return render(request,'registro.html')
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

def vistajuego(request):
    perfil = mod.Perfil.objects.get(usuario = request.user)
    SeleccionEnemigo = mod.Enemigo.objects.get(nivel = perfil.victorias)
    enemigo_asignado = mod.EnemigoAsignado.objects.create(nivel = SeleccionEnemigo.nivel, nombre =SeleccionEnemigo.nombre, vida = SeleccionEnemigo.vida,
    daño = SeleccionEnemigo.daño, defensa = SeleccionEnemigo.defensa, imagen = SeleccionEnemigo.imagen)
    perfil.enemigoAsignado = enemigo_asignado
    perfil.save()
    enemigo = perfil.enemigoAsignado
    enemigoAsignado = mod.EnemigoAsignado.objects.get(perfil = perfil)

    RegistroPosionesVida = mod.PosionPerfil.objects.filter(perfil = perfil, posion__nombre ='pócima de vida' )
    RegistroPosionesDaño = mod.PosionPerfil.objects.filter(perfil = perfil, posion__nombre ='pócima de daño' )
    perfil.vida_actual = perfil.vida_total
    perfil.save()
    clase = perfil.clase
    contexto = {
        'posionesVida' : RegistroPosionesVida,
        'posionesDaño' : RegistroPosionesDaño,
        'SeleccionEnemigo' : SeleccionEnemigo,
        'enemigo' : enemigo,
        'perfil' : perfil,
        'clase' : clase
    }
    return render(request,'juego.html',contexto)

def atacar(request):
    perfil = mod.Perfil.objects.get(usuario = request.user)
    enemigoAsignado = mod.EnemigoAsignado.objects.get(perfil= perfil)

    if(enemigoAsignado.vida > 0 ):
        enemigoAsignado.vida = enemigoAsignado.vida-perfil.daño_total
        enemigoAsignado.save()
        data = enemigoAsignado.vida
        return HttpResponse(data)
    

def ataqueEnemigo(request):
    perfil = mod.Perfil.objects.get(usuario = request.user)
    enemigoAsignado = mod.EnemigoAsignado.objects.get(perfil= perfil)
    if(perfil.vida_actual > 0):
        perfil.vida_actual = perfil.vida_actual-enemigoAsignado.daño
        perfil.save()
        data = perfil.vida_actual
        return HttpResponse(data)

def usarPosionVida(request):
    perfil = mod.Perfil.objects.get(usuario = request.user)
    RegistroPosionesVida = mod.PosionPerfil.objects.filter(perfil = perfil, posion__nombre ='pócima de vida' ).first()
    vidaRestaurada = perfil.vida_actual+RegistroPosionesVida.posion.vida
    if(perfil.vida_actual > 0 and vidaRestaurada <= perfil.vida_total):
        perfil.vida_actual = perfil.vida_actual+RegistroPosionesVida.posion.vida
        perfil.posion.remove(RegistroPosionesVida)
        perfil.save()
        data = perfil.vida_actual
        return HttpResponse(data)

def usarPosionDaño(request):
    perfil = mod.Perfil.objects.get(usuario = request.user)
    RegistroPosionesDaño= mod.PosionPerfil.objects.filter(perfil = perfil, posion__nombre ='pócima de daño' ).first()
    dañoAumentado = perfil.daño_total+RegistroPosionesDaño.posion.daño
    if(perfil.vida_actual > 0 ):
        perfil.daño_total = dañoAumentado
        perfil.posion.remove(RegistroPosionesDaño)
        perfil.save()
        data = perfil.daño_total
        return HttpResponse(data)

def vistaGanaste(request):
    perfil = mod.Perfil.objects.get(usuario = request.user)
    perfil.victorias = perfil.victorias +1
    recompensa = mod.Recompensa.objects.get(nivel = perfil.victorias)
    perfil.recompensa.add(recompensa)
    perfil.save()
    recompensaActiva= mod.Recompensa.objects.get(perfil__usuario = request.user, nivel = perfil.victorias)
    nuevoPrecio = recompensaActiva.obtenerNuevoPrecio()
    contexto = {"descuento" : recompensaActiva.descuento,
                 "producto" : recompensaActiva.Producto,
                 "nuevoPrecio" : nuevoPrecio}
    return render(request,'ganaste!.html',contexto)



