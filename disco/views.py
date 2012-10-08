# Create your views here.
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template.context import RequestContext
from disco.models import *
from usuario.models import UsuarioRegistrado
from disco.forms import DiscoForm,ComposicionDiscoForm, TemaBandaForm, TemaForm
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
        tema_banda=composicion_disco.tema_banda
        tema=tema_banda.tema
        composicion_disco.delete()
        tema_banda.delete()
        tema.delete()
    nombre_disco=disco.nombre
    disco.delete()
    messages.success(request, 'Se elimino correctamente el disco "%s".' % nombre_disco)     
    return HttpResponseRedirect(reverse('banda.views.administrar', kwargs={'banda_id':banda_id}))

@login_required(login_url='/usuario/login/')
def nuevo_composicion_disco(request,disco_id):
    usuario_registrado=UsuarioRegistrado.objects.get(pk=request.user.id)
    disco=Disco.objects.get(pk=disco_id)
    if request.method == 'POST':
        form_tema= TemaForm(request.POST)
        form_tema_banda= TemaBandaForm(request.POST)
        form_composicion_disco= ComposicionDiscoForm(request.POST)
        if form_tema.is_valid() and form_tema_banda.is_valid() and form_composicion_disco.is_valid():
            composicion_disco=form_composicion_disco.save(commit=False)
            composicion_disco.disco=disco
            tema_banda=form_tema_banda.save(commit=False)
            tema=form_tema.save()
            tema_banda.banda=disco.banda
            tema_banda.tema=tema
            tema_banda.save()
            composicion_disco.tema_banda=tema_banda;
            composicion_disco.save()
            messages.success(request, 'Se agrego correctamente el tema "%(tema)s" al disco "%(disco)s".' % {'tema': tema.nombre, 'disco': disco.nombre})
            return HttpResponseRedirect(reverse('disco.views.administrar', kwargs={'disco_id':disco_id}))
    else:
        form_composicion_disco= ComposicionDiscoForm()
        form_tema= TemaForm()
        form_tema_banda= TemaBandaForm()
    return render_to_response("disco/nuevo_composicion_disco.html", locals(), context_instance=RequestContext(request))



@login_required(login_url='/usuario/login/')
def modificar_composicion_disco(request,composicion_disco_id):
    usuario_registrado=UsuarioRegistrado.objects.get(pk=request.user.id)
    composicion_disco=ComposicionDisco.objects.get(pk=composicion_disco_id)
    if request.method == 'POST':
        form_composicion_disco = ComposicionDiscoForm(request.POST,instance=composicion_disco)
        form_tema = TemaForm(request.POST, instance=composicion_disco.tema_banda.tema)
        form_tema_banda = TemaBandaForm(request.POST,instance=composicion_disco.tema_banda)
        if form_tema.is_valid() and form_tema_banda.is_valid() and form_composicion_disco.is_valid():
            tema_banda=form_tema_banda.save(commit=False)
            composicion_disco=form_composicion_disco.save(commit=False)
            tema=form_tema.save()
            tema_banda.tema=tema
            tema_banda.save()
            composicion_disco.tema_banda=tema_banda;
            composicion_disco.save()
            messages.success(request, 'Se modifico correctamente el tema "%(tema)s" del disco "%(disco)s".' % {'tema': composicion_disco.tema_banda.tema.nombre, 'disco': composicion_disco.disco.nombre})
            return HttpResponseRedirect(reverse('disco.views.administrar', kwargs={'disco_id':composicion_disco.disco.id}))
    else:
        form_composicion_disco= ComposicionDiscoForm(instance=composicion_disco)
        form_tema_banda= TemaBandaForm(instance=composicion_disco.tema_banda)
        form_tema = TemaForm(instance=composicion_disco.tema_banda.tema)
    return render_to_response("disco/modificar_composicion_disco.html", locals(), context_instance=RequestContext(request))

@login_required(login_url='/usuario/login/')        
def eliminar_composicion_disco(request,composicion_disco_id):
    composicion_disco=ComposicionDisco.objects.get(pk=composicion_disco_id)
    disco_id=composicion_disco.disco.id
    tema_banda=composicion_disco.tema_banda
    tema=tema_banda.tema
    nombre_tema=tema.nombre
    nombre_disco=composicion_disco.disco.nombre
    composicion_disco.delete()
    tema_banda.delete()
    tema.delete()
    messages.success(request, 'Se elimino correctamente el tema "%(tema)s" del disco "%(disco)s".' % {'tema': nombre_tema , 'disco': nombre_disco})
    return HttpResponseRedirect(reverse('disco.views.administrar', kwargs={'disco_id':disco_id}))
