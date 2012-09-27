# Create your views here.
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template.context import RequestContext
from usuario.models import UsuarioRegistrado 
from suscripcion.models import *
from suscripcion.forms import *
from django.contrib.auth.decorators import login_required
from django.contrib import messages


@login_required(login_url='/usuario/login/')
def listado(request):
    if request.user.is_authenticated():
        usuario_registrado=UsuarioRegistrado.objects.get(pk=request.user.id)
    suscripciones_banda=SuscripcionBanda.objects.filter(usuario__id=request.user.id)
    suscripciones_complejo=SuscripcionComplejo.objects.filter(usuario__id=request.user.id)
    suscripciones_musico=SuscripcionMusico.objects.filter(usuario__id=request.user.id)
    suscripciones_genero=SuscripcionGenero.objects.filter(usuario__id=request.user.id)
    return render_to_response("suscripcion/listado.html", locals(), context_instance=RequestContext(request))

@login_required(login_url='/usuario/login/')
def modificar_genero(request,genero_id):
    if request.user.is_authenticated():
        usuario_registrado=UsuarioRegistrado.objects.get(pk=request.user.id)
    suscripcion=SuscripcionGenero.objects.get(genero__id=genero_id, usuario__id=request.user.id)
    if request.method == 'POST':
        form = SuscripcionGeneroForm(request.POST, instance=suscripcion)
        if form.is_valid():
            form.save()
            messages.success(request, 'Se modifico correctamente la suscripcion al genero "%s".' % suscripcion.genero.nombre)
            return HttpResponseRedirect(reverse('suscripcion.views.listado'))
    else:
        form = SuscripcionGeneroForm(instance=suscripcion)
    return render_to_response("suscripcion/modificar_genero.html", locals(), context_instance=RequestContext(request))   

@login_required(login_url='/usuario/login/')
def eliminar_genero(request,genero_id):
    suscripcion=SuscripcionGenero.objects.get(genero__id=genero_id, usuario__id=request.user.id)
    suscripcion.delete()
    messages.success(request, 'Se borro correctamente la suscripcion al genero "%s".' % suscripcion.genero.nombre)
    return HttpResponseRedirect(reverse('suscripcion.views.listado'))

@login_required(login_url='/usuario/login/')
def modificar_banda(request,banda_id):
    if request.user.is_authenticated():
        usuario_registrado=UsuarioRegistrado.objects.get(pk=request.user.id)
    suscripcion=SuscripcionBanda.objects.get(banda__id=banda_id, usuario__id=request.user.id)
    if request.method == 'POST':
        form = SuscripcionBandaForm(request.POST, instance=suscripcion)
        if form.is_valid():
            form.save()
            messages.success(request, 'Se modifico correctamente la suscripcion a la banda "%s".' % suscripcion.banda.nombre)
            return HttpResponseRedirect(reverse('suscripcion.views.listado'))
    else:
        form = SuscripcionBandaForm(instance=suscripcion)
    return render_to_response("suscripcion/modificar_banda.html", locals(), context_instance=RequestContext(request))   
    
@login_required(login_url='/usuario/login/')
def eliminar_banda(request,banda_id):
    suscripcion=SuscripcionBanda.objects.get(banda__id=banda_id, usuario__id=request.user.id)
    suscripcion.delete()
    messages.success(request, 'Se borro correctamente la suscripcion a la banda "%s".' % suscripcion.banda.nombre)
    return HttpResponseRedirect(reverse('suscripcion.views.listado'))

    
@login_required(login_url='/usuario/login/')
def modificar_musico(request,musico_id):
    if request.user.is_authenticated():
        usuario_registrado=UsuarioRegistrado.objects.get(pk=request.user.id)
    suscripcion=SuscripcionMusico.objects.get(musico__id=musico_id, usuario__id=request.user.id)
    if request.method == 'POST':
        form = SuscripcionMusicoForm(request.POST, instance=suscripcion)
        if form.is_valid():
            form.save()
            messages.success(request, 'Se modifico correctamente la suscripcion del musico "%(nombre)s, %(apellido)s".' % {'nombre': suscripcion.musico.first_name, 'apellido': suscripcion.musico.last_name})
            return HttpResponseRedirect(reverse('suscripcion.views.listado'))
    else:
        form = SuscripcionMusicoForm(instance=suscripcion)
    return render_to_response("suscripcion/modificar_musico.html", locals(), context_instance=RequestContext(request))   
    
@login_required(login_url='/usuario/login/')
def eliminar_musico(request,musico_id):
    suscripcion=SuscripcionMusico.objects.get(musico__id=musico_id, usuario__id=request.user.id)
    suscripcion.delete()
    messages.success(request, 'Se borro correctamente la suscripcion del musico "%(nombre)s, %(apellido)s".' % {'nombre': suscripcion.musico.first_name, 'apellido': suscripcion.musico.last_name})
    return HttpResponseRedirect(reverse('suscripcion.views.listado'))

@login_required(login_url='/usuario/login/')
def modificar_complejo(request,complejo_id):
    if request.user.is_authenticated():
        usuario_registrado=UsuarioRegistrado.objects.get(pk=request.user.id)
    suscripcion=SuscripcionComplejo.objects.get(complejo__id=complejo_id, usuario__id=request.user.id)
    if request.method == 'POST':
        form = SuscripcionComplejoForm(request.POST, instance=suscripcion)
        if form.is_valid():
            form.save()
            messages.success(request, 'Se modifico correctamente la suscripcion al complejo "%s".' % suscripcion.complejo.nombre)
            return HttpResponseRedirect(reverse('suscripcion.views.listado'))
    else:
        form = SuscripcionComplejoForm(instance=suscripcion)
    return render_to_response("suscripcion/modificar_complejo.html", locals(), context_instance=RequestContext(request))   
            
@login_required(login_url='/usuario/login/')
def eliminar_complejo(request,complejo_id):
    suscripcion=SuscripcionComplejo.objects.get(complejo__id=complejo_id, usuario__id=request.user.id)
    suscripcion.delete()
    messages.success(request, 'Se borro correctamente la suscripcion al complejo "%s".' % suscripcion.complejo.nombre)
    return HttpResponseRedirect(reverse('suscripcion.views.listado'))
    