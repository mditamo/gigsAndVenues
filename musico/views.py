# Create your views here.
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from banda.models import ComposicionBanda, EstadoComposicionBanda
from musico.models import *
from equipo.models import EquipoMusico
from usuario.models import UsuarioRegistrado
from django.db.models import Q
from musico.forms import MusicoForm
from direccion.forms import DireccionForm
from genero.models import Genero

from django.contrib.auth.decorators import permission_required


def ver(request,musico_id):
    if request.user.is_authenticated():
        usuario_registrado=UsuarioRegistrado.objects.get(pk=request.user.id)
    musico=Musico.objects.get(pk=request.user.id)
    equipos_musico=EquipoMusico.objects.filter(musico=request.user)
    estado=EstadoComposicionBanda.objects.get(nombre="Confirmado")
    composiciones_banda_actuales=ComposicionBanda.objects.filter(Q(musico=request.user), Q(estado_id=estado))
    composiciones_banda_anteriores=ComposicionBanda.objects.filter(Q(musico=request.user), ~Q(estado_id=estado))
    generos=Genero.objects.raw('Select distinct g.* from GENERO g join BANDA_GENERO bg ON bg.GENERO_ID=g.ID join COMPOSICION_BANDA cb ON cb.BANDA_ID=bg.BANDA_ID WHERE cb.MUSICO_ID=%s',[musico_id])
    return render_to_response("musico/ver.html", locals(), context_instance=RequestContext(request))


def equipos(request):
    equipos_musico=EquipoMusico.objects.filter(musico=request.user)
    if request.user.is_authenticated():
        usuario_registrado=UsuarioRegistrado.objects.get(pk=request.user.id)
    return render_to_response("musico/equipos.html", locals(), context_instance=RequestContext(request))

def perfil(request):
    if request.user.is_authenticated():
        usuario_registrado=UsuarioRegistrado.objects.get(pk=request.user.id)
    musico=Musico.objects.get(pk=request.user.id)
    return render_to_response("musico/perfil.html", locals(), context_instance=RequestContext(request))

def modificar(request,musico_id):
    if request.user.is_authenticated():
        usuario_registrado=UsuarioRegistrado.objects.get(pk=request.user.id)
    musico=Musico.objects.get(pk=musico_id)
    if request.method == 'POST':
        form = MusicoForm(request.POST, instance=musico)
        if form.is_valid():
            musico.save()
        return render_to_response("musico/perfil.html", locals(), context_instance=RequestContext(request))
    else:
        form = MusicoForm(instance=musico)
        form_dir = DireccionForm(instance=musico.direccion)
        return render_to_response("musico/modificar.html", locals(), context_instance=RequestContext(request))
