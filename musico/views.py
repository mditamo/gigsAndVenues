# Create your views here.
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template.context import RequestContext
from banda.models import ComposicionBanda, EstadoComposicionBanda
from musico.models import *
from musico.forms import *
from equipo.models import EquipoMusico
from usuario.models import UsuarioRegistrado
from django.db.models import Q
from suscripcion.models import SuscripcionMusico
from suscripcion.forms import SuscripcionMusicoForm
from direccion.forms import DireccionForm
from genero.models import Genero
from suscripcion.models import SuscripcionBanda, SuscripcionGenero
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def ver(request,musico_id):
    if request.user.is_authenticated():
        usuario_registrado=UsuarioRegistrado.objects.get(pk=request.user.id)
    form_suscripcion = SuscripcionMusicoForm()    
    musico=Musico.objects.get(pk=musico_id)
    equipos_musico=EquipoMusico.objects.filter(musico__id=musico_id)
    suscripciones_banda=SuscripcionBanda.objects.filter(usuario__id=musico_id)
    suscripciones_genero=SuscripcionGenero.objects.filter(usuario__id=musico_id)
    estado_confirmado=EstadoComposicionBanda.objects.get(nombre="Confirmado")
    estado_eliminado=EstadoComposicionBanda.objects.get(nombre="Eliminado")
    composiciones_banda_actuales=ComposicionBanda.objects.filter(Q(musico__id=musico_id), Q(estado_id=estado_confirmado))
    composiciones_banda_anteriores=ComposicionBanda.objects.filter(Q(musico__id=musico_id), Q(estado_id=estado_eliminado))
    cantidad_like=LikeMusico.objects.filter(musico__id=musico_id, usuario__id=request.user.id).count()
    cantidad_seguidores=LikeMusico.objects.filter(musico__id=musico_id).count()
    cantidad_suscripcion=SuscripcionMusico.objects.filter(musico__id=musico_id, usuario__id=request.user.id).count()
    generos=Genero.objects.raw('Select distinct g.* from GENERO g join BANDA_GENERO bg ON bg.GENERO_ID=g.ID join COMPOSICION_BANDA cb ON cb.BANDA_ID=bg.BANDA_ID WHERE cb.MUSICO_ID=%s',[musico_id])
    return render_to_response("musico/ver.html", locals(), context_instance=RequestContext(request))

@login_required(login_url='/usuario/login/')
def perfil(request):
    if request.user.is_authenticated():
        usuario_registrado=UsuarioRegistrado.objects.get(pk=request.user.id)
    musico=Musico.objects.get(pk=request.user.id)
    return render_to_response("musico/perfil.html", locals(), context_instance=RequestContext(request))

@login_required(login_url='/usuario/login/')
def modificar(request,musico_id):
    if request.user.is_authenticated():
        usuario_registrado=UsuarioRegistrado.objects.get(pk=request.user.id)
    musico=Musico.objects.get(pk=musico_id)
    if request.method == 'POST':
        form_dir = DireccionForm(request.POST)
        form = MusicoForm(request.POST, instance=musico)
        if form.is_valid() and form_dir.is_valid():
            musico=form.save(commit=False)
            direccion=form_dir.save()
            musico.direccion=direccion
            musico.save()
            messages.success(request, 'Se modifico correctamente los datos del musico "%(nombre)s, %(apellido)s".' % {'nombre': musico.first_name, 'apellido': musico.last_name})
            return render_to_response("musico/perfil.html", locals(), context_instance=RequestContext(request))
    else:
        form = MusicoForm(instance=musico)
        form_dir = DireccionForm(instance=musico.direccion)
    return render_to_response("musico/modificar.html", locals(), context_instance=RequestContext(request))


@login_required(login_url='/usuario/login/')
def like(request,musico_id):
    like = LikeMusico.objects.create(musico_id=musico_id, usuario_id=request.user.id)
    like.save()
    return HttpResponseRedirect(reverse('musico.views.ver', kwargs={'musico_id':musico_id}))

@login_required(login_url='/usuario/login/')
def no_like(request,musico_id):
    like=LikeMusico.objects.filter(musico__id=musico_id, usuario__id=request.user.id)
    like.delete()
    return HttpResponseRedirect(reverse('musico.views.ver', kwargs={'musico_id':musico_id}))

@login_required(login_url='/usuario/login/')
def suscribirme(request,musico_id):
    form = SuscripcionMusicoForm(request.POST)
    suscripcion=form.save(commit=False)
    if form.is_valid():
        suscripcion.musico=Musico.objects.get(pk=musico_id)
        suscripcion.usuario=UsuarioRegistrado.objects.get(pk=request.user.id)
        suscripcion.save()
    return HttpResponseRedirect(reverse('musico.views.ver', kwargs={'musico_id':musico_id}))

@login_required(login_url='/usuario/login/')
def no_suscribirme(request,musico_id):
    suscripcion=SuscripcionMusico.objects.filter(musico__id=musico_id, usuario__id=request.user.id)
    suscripcion.delete()
    return HttpResponseRedirect(reverse('musico.views.ver', kwargs={'musico_id':musico_id}))