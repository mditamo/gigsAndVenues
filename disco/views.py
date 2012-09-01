# Create your views here.
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template.context import RequestContext
from disco.models import *
from usuario.models import UsuarioRegistrado
from disco.forms import DiscoForm

def ver(request,disco_id):
    usuario_registrado=UsuarioRegistrado.objects.get(pk=request.user.id)
    disco=Disco.objects.get(pk=disco_id)
    composiciones_disco=ComposicionDisco.objects.filter(disco__id=disco_id)
    return render_to_response("disco/ver.html", locals(), context_instance=RequestContext(request))

def nuevo(request,banda_id):
    usuario_registrado=UsuarioRegistrado.objects.get(pk=request.user.id)
    banda=Banda.objects.get(pk=banda_id)
    if request.method == 'POST':
        form = DiscoForm(request.POST)
        disco=form.save(commit=False)
        if form.is_valid():
            disco.banda=banda
            disco.save()
        return HttpResponseRedirect(reverse('banda.views.ver', kwargs={'banda_id':banda_id}))
    else:
        form= DiscoForm()
        return render_to_response("disco/nuevo.html", locals(), context_instance=RequestContext(request))

def modificar(request,disco_id):
    usuario_registrado=UsuarioRegistrado.objects.get(pk=request.user.id)
    disco=Disco.objects.get(pk=disco_id)
    if request.method == 'POST':
        form = DiscoForm(request.POST,instance=disco)
        disco=form.save(commit=False)
        if form.is_valid():
            disco.save()
        return HttpResponseRedirect(reverse('banda.views.ver', kwargs={'banda_id':disco.banda.id}))
    else:
        form= DiscoForm(instance=disco)
        return render_to_response("disco/modificar.html", locals(), context_instance=RequestContext(request))

def nuevo_tema(request,disco_id):
    usuario_registrado=UsuarioRegistrado.objects.get(pk=request.user.id)
    disco=Disco.objects.get(pk=disco_id)
    return render_to_response("disco/nuevo_tema.html", locals(), context_instance=RequestContext(request))
	
	
	
	