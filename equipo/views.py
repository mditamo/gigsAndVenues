# Create your views here.
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template.context import RequestContext
from usuario.models import UsuarioRegistrado
from equipo.models import EquipoMusico
from equipo.forms import EquipoMusicoForm
from musico.models import Musico


def listado(request):
    equipos_musico=EquipoMusico.objects.filter(musico=request.user)
    usuario_registrado=UsuarioRegistrado.objects.get(pk=request.user.id)
    return render_to_response("equipo/listado.html", locals(), context_instance=RequestContext(request))

def nuevo(request):
    usuario_registrado=UsuarioRegistrado.objects.get(pk=request.user.id)
    musico=Musico.objects.get(pk=request.user.id)
    if request.method == 'POST':
        form = EquipoMusicoForm(request.POST)
        equipo_musico=form.save(commit=False)
        if form.is_valid():
            equipo_musico.musico=musico
            equipo_musico.save()
        return HttpResponseRedirect(reverse('equipo.views.listado', kwargs={}))
    else:
        form= EquipoMusicoForm()
        return render_to_response("equipo/nuevo.html", locals(), context_instance=RequestContext(request))

    
def eliminar(request,equipo_musico_id):
    equipo_musico=EquipoMusico.objects.get(pk=equipo_musico_id)
    equipo_musico.delete()
    return HttpResponseRedirect(reverse('equipo.views.listado', kwargs={}))
    
def modificar(request,equipo_musico_id):    
    usuario_registrado=UsuarioRegistrado.objects.get(pk=request.user.id)
    equipo_musico=EquipoMusico.objects.get(pk=equipo_musico_id)
    if request.method == 'POST':
        form = EquipoMusicoForm(request.POST,instance=equipo_musico)
        equipo_musico=form.save(commit=False)
        if form.is_valid():
            equipo_musico.save()
        return HttpResponseRedirect(reverse('equipo.views.listado', kwargs={}))
    else:
        form= EquipoMusicoForm(instance=equipo_musico)
        return render_to_response("equipo/modificar.html", locals(), context_instance=RequestContext(request))
