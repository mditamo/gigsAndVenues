# Create your views here.
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template.context import RequestContext
from disco.models import *
from usuario.models import UsuarioRegistrado
from disco.forms import DiscoForm,ComposicionDiscoForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required(login_url='/usuario/login/')
def administrar(request,disco_id):
    usuario_registrado=UsuarioRegistrado.objects.get(pk=request.user.id)
    disco=Disco.objects.get(pk=disco_id)
    composiciones_disco=ComposicionDisco.objects.filter(disco__id=disco_id)
    return render_to_response("disco/administrar.html", locals(), context_instance=RequestContext(request))

def ver(request,disco_id):
    usuario_registrado=UsuarioRegistrado.objects.get(pk=request.user.id)
    disco=Disco.objects.get(pk=disco_id)
    composiciones_disco=ComposicionDisco.objects.filter(disco__id=disco_id)
    return render_to_response("disco/ver.html", locals(), context_instance=RequestContext(request))

@login_required(login_url='/usuario/login/')
def nuevo(request,banda_id):
    usuario_registrado=UsuarioRegistrado.objects.get(pk=request.user.id)
    banda=Banda.objects.get(pk=banda_id)
    if request.method == 'POST':
        form = DiscoForm(request.POST)
        disco=form.save(commit=False)
        if form.is_valid():
            disco.banda=banda
            disco.save()
            messages.success(request, 'Se agrego correctamente el disco "%s".' % disco.nombre)
            return HttpResponseRedirect(reverse('banda.views.administrar', kwargs={'banda_id':banda_id}))
    else:
        form= DiscoForm()
    return render_to_response("disco/nuevo.html", locals(), context_instance=RequestContext(request))

@login_required(login_url='/usuario/login/')
def modificar(request,disco_id):
    usuario_registrado=UsuarioRegistrado.objects.get(pk=request.user.id)
    disco=Disco.objects.get(pk=disco_id)
    if request.method == 'POST':
        form = DiscoForm(request.POST,instance=disco)
        disco=form.save(commit=False)
        if form.is_valid():
            disco.save()
            messages.success(request, 'Se modifico correctamente el disco "%s".' % disco.nombre)
            return HttpResponseRedirect(reverse('banda.views.administrar', kwargs={'banda_id':disco.banda.id}))
    else:
        form= DiscoForm(instance=disco)
    return render_to_response("disco/modificar.html", locals(), context_instance=RequestContext(request))

@login_required(login_url='/usuario/login/')
def eliminar(request, disco_id):
    disco=Disco.objects.get(pk=disco_id)
    banda_id=disco.banda.id
    composiciones_disco=ComposicionDisco.objects.filter(disco__id=disco_id)
    for composicion_disco in composiciones_disco:
        composicion_disco.delete()
    nombre_disco=disco.nombre
    disco.delete()
    messages.success(request, 'Se elimino correctamente el disco "%s".' % nombre_disco)     
    return HttpResponseRedirect(reverse('banda.views.administrar', kwargs={'banda_id':banda_id}))

@login_required(login_url='/usuario/login/')
def nuevo_composicion_disco(request,disco_id):
    usuario_registrado=UsuarioRegistrado.objects.get(pk=request.user.id)
    disco=Disco.objects.get(pk=disco_id)
    if request.method == 'POST':
        form= ComposicionDiscoForm(request.POST)
        if form.is_valid():
            composicion_disco=form.save(commit=False)
            composicion_disco.disco=disco
            composicion_disco.save()
            messages.success(request, 'Se agrego correctamente el tema "%(tema)s" al disco "%(disco)s".' % {'tema': composicion_disco.tema_banda.tema.nombre, 'disco': disco.nombre})
            return HttpResponseRedirect(reverse('disco.views.administrar', kwargs={'disco_id':disco_id}))
    else:
        form= ComposicionDiscoForm()
    return render_to_response("disco/nuevo_composicion_disco.html", locals(), context_instance=RequestContext(request))
    
@login_required(login_url='/usuario/login/')
def modificar_composicion_disco(request,composicion_disco_id):
    usuario_registrado=UsuarioRegistrado.objects.get(pk=request.user.id)
    composicion_disco=ComposicionDisco.objects.get(pk=composicion_disco_id)
    if request.method == 'POST':
        form = ComposicionDiscoForm(request.POST,instance=composicion_disco)
        if form.is_valid():
            form.save()
            messages.success(request, 'Se modifico correctamente el tema "%(tema)s" del disco "%(disco)s".' % {'tema': composicion_disco.tema_banda.tema.nombre, 'disco': composicion_disco.disco.nombre})
            return HttpResponseRedirect(reverse('disco.views.administrar', kwargs={'disco_id':composicion_disco.disco.id}))
    else:
        form= ComposicionDiscoForm(instance=composicion_disco)
    return render_to_response("disco/modificar_composicion_disco.html", locals(), context_instance=RequestContext(request))

@login_required(login_url='/usuario/login/')        
def eliminar_composicion_disco(request,composicion_disco_id):
    composicion_disco=ComposicionDisco.objects.get(pk=composicion_disco_id)
    disco_id=composicion_disco.disco.id
    nombre_tema=composicion_disco.tema_banda.tema.nombre
    nombre_disco=composicion_disco.disco.nombre
    composicion_disco.delete()
    messages.success(request, 'Se elimino correctamente el tema "%(tema)s" del disco "%(disco)s".' % {'tema': nombre_tema , 'disco': nombre_disco})
    return HttpResponseRedirect(reverse('disco.views.administrar', kwargs={'disco_id':disco_id}))
