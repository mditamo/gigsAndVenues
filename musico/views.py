# Create your views here.
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from banda.models import ComposicionBanda, EstadoComposicionBanda
from musico.models import *
from usuario.models import UsuarioRegistrado
from django.db.models import Q
from musico.forms import MusicoForm
from direccion.forms import DireccionForm

from django.contrib.auth.decorators import permission_required

def listado_bandas(request):
    """composiciones_banda=ComposicionBanda.objects.filter(musico=request.user).filter(estado!=EstadoComposicionBanda.objects.get(nombre="Eliminado"))"""
    estado=EstadoComposicionBanda.objects.get(nombre="Eliminado")
    composiciones_banda=ComposicionBanda.objects.filter(Q(musico=request.user), ~Q(estado_id=estado))

    usuario_registrado=UsuarioRegistrado.objects.get(pk=request.user.id)
    return render_to_response("banda/listado.html", locals(), context_instance=RequestContext(request))

def equipos(request):
    equipos_musico=EquipoMusico.objects.filter(musico=request.user)
    usuario_registrado=UsuarioRegistrado.objects.get(pk=request.user.id)
    return render_to_response("musico/equipos.html", locals(), context_instance=RequestContext(request))

def perfil(request):
    usuario_registrado=UsuarioRegistrado.objects.get(pk=request.user.id)
    musico=Musico.objects.get(pk=request.user.id)
    return render_to_response("musico/perfil.html", locals(), context_instance=RequestContext(request))

def modificar(request,musico_id):
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
