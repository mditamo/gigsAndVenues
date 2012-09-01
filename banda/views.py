# Create your views here.
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template.context import RequestContext
from banda.models import *
from disco.models import Disco,TemaBanda
from musico.models import Musico
from usuario.models import UsuarioRegistrado
from banda.forms import *

def ver(request,banda_id):
    usuario_registrado=UsuarioRegistrado.objects.get(pk=request.user.id)
    banda=Banda.objects.get(pk=banda_id)
    generos_banda=BandaGenero.objects.filter(banda__id=banda_id)
    composiciones_banda=ComposicionBanda.objects.filter(banda__id=banda_id)
    temas_banda=TemaBanda.objects.filter(banda__id=banda_id)
    discos=Disco.objects.filter(banda__id=banda_id)
    return render_to_response("banda/ver.html", locals(), context_instance=RequestContext(request))
	
def confirmar(request,banda_id,musico_id):
    composicion_banda=ComposicionBanda.objects.get(banda__id=banda_id, musico__id=musico_id)
    composicion_banda.estado=EstadoComposicionBanda.objects.get(nombre="Confirmado")
    composicion_banda.save()
    return HttpResponseRedirect(reverse('banda.views.ver', kwargs={'banda_id':banda_id}))

def denegar(request,banda_id,musico_id):
    composicion_banda=ComposicionBanda.objects.get(banda__id=banda_id, musico__id=musico_id)
    composicion_banda.estado=EstadoComposicionBanda.objects.get(nombre="Denegado")
    composicion_banda.save()
    return HttpResponseRedirect(reverse('banda.views.ver', kwargs={'banda_id':banda_id}))

def eliminar(request,banda_id,musico_id):
    composicion_banda=ComposicionBanda.objects.get(banda__id=banda_id, musico__id=musico_id)
    composicion_banda.estado=EstadoComposicionBanda.objects.get(nombre="Eliminado")
    composicion_banda.save()
    return HttpResponseRedirect(reverse('banda.views.ver', kwargs={'banda_id':banda_id}))

def modificar(request,banda_id):
    usuario_registrado=UsuarioRegistrado.objects.get(pk=request.user.id)
    banda=Banda.objects.get(pk=banda_id)
    if request.method == 'POST':
        form = BandaForm(request.POST, instance=banda)
        banda.generos.clear()
        if form.is_valid():
            for genero_id in request.POST.getlist('generos'):
                banda_genero = BandaGenero.objects.create(banda_id=banda_id, genero_id=genero_id)
                banda_genero.save()
        banda.save()
        return HttpResponseRedirect(reverse('musico.views.listado_bandas'))
    else:
        form = BandaForm(instance=banda)
        return render_to_response("banda/modificar.html", locals(), context_instance=RequestContext(request))

def nuevo(request):
    usuario_registrado=UsuarioRegistrado.objects.get(pk=request.user.id)
    musico=Musico.objects.get(pk=request.user.id)
    if request.method == 'POST':
        form = BandaForm(request.POST)
        banda=form.save(commit=False)
        if form.is_valid():
            banda.save()
            for genero_id in request.POST.getlist('generos'):
                banda_genero = BandaGenero.objects.create(banda_id=banda.id, genero_id=genero_id)
                banda_genero.save()
            estado=EstadoComposicionBanda.objects.get(nombre="Confirmado")
            composicion_banda=ComposicionBanda(musico_id=musico.id,banda_id=banda.id,estado=estado)
            composicion_banda.save()
        return HttpResponseRedirect(reverse('musico.views.listado_bandas'))
    else:
        form = BandaForm()
        return render_to_response("banda/nuevo.html", locals(), context_instance=RequestContext(request))


def modificar_composicion_banda(request,banda_id,musico_id):
    usuario_registrado=UsuarioRegistrado.objects.get(pk=request.user.id)
    composicion_banda=ComposicionBanda.objects.get(banda__id=banda_id, musico__id=musico_id)

    if request.method == 'POST':
        form = ComposicionBandaForm(request.POST, instance=composicion_banda)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('banda.views.ver', kwargs={'banda_id':banda_id}))
    else:
        form = ComposicionBandaForm(instance=composicion_banda)
        return render_to_response("banda/modificar_composicion_banda.html", locals(), context_instance=RequestContext(request))

