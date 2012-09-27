# Create your views here.
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template.context import RequestContext
from usuario.models import UsuarioRegistrado
from fan.models import Fan
from fan.forms import FanForm
from direccion.forms import DireccionForm
from suscripcion.models import SuscripcionBanda, SuscripcionGenero
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def ver(request,fan_id):
    if request.user.is_authenticated():
        usuario_registrado=UsuarioRegistrado.objects.get(pk=request.user.id)
    fan=Fan.objects.get(pk=fan_id)    
    suscripciones_banda=SuscripcionBanda.objects.filter(usuario__id=fan_id)
    suscripciones_genero=SuscripcionGenero.objects.filter(usuario__id=fan_id)
    return render_to_response("fan/ver.html", locals(), context_instance=RequestContext(request))

@login_required(login_url='/usuario/login/')
def perfil(request):
    if request.user.is_authenticated():
        usuario_registrado=UsuarioRegistrado.objects.get(pk=request.user.id)
    fan=Fan.objects.get(pk=request.user.id)
    return render_to_response("fan/perfil.html", locals(), context_instance=RequestContext(request))

@login_required(login_url='/usuario/login/')
def modificar(request,fan_id):
    if request.user.is_authenticated():
        usuario_registrado=UsuarioRegistrado.objects.get(pk=request.user.id)
    fan=Fan.objects.get(pk=fan_id)
    if request.method == 'POST':
        form_dir = DireccionForm(request.POST)
        form = FanForm(request.POST, instance=fan)
        if form.is_valid() and form_dir.is_valid():
            fan=form.save(commit=False)
            direccion=form_dir.save()
            fan.direccion=direccion
            fan.save()
            messages.success(request, 'Se modifico correctamente los datos del fan "%(nombre)s, %(apellido)s".' % {'nombre': fan.first_name, 'apellido': fan.last_name})
            return render_to_response("fan/perfil.html", locals(), context_instance=RequestContext(request))
    else:
        form = FanForm(instance=fan)
        form_dir = DireccionForm(instance=fan.direccion)
    return render_to_response("fan/modificar.html", locals(), context_instance=RequestContext(request))

