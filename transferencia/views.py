# Create your views here.
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template.context import RequestContext
from usuario.models import UsuarioRegistrado
from django.contrib.auth.decorators import login_required

@login_required(login_url='/usuario/login/')
def index(request):
    if request.user.is_authenticated():
        usuario_registrado=UsuarioRegistrado.objects.get(pk=request.user.id)
    if usuario_registrado.is_fan():
        return HttpResponseRedirect('/transferencia/fan')
    if usuario_registrado.is_musico():
        return HttpResponseRedirect('/transferencia/musico')
    if usuario_registrado.is_complejo():
        return HttpResponseRedirect('/transferencia/complejo')

@login_required(login_url='/usuario/login/')
def fan(request):
    if request.user.is_authenticated():
        usuario_registrado=UsuarioRegistrado.objects.get(pk=request.user.id)
    return render_to_response("transferencia/fan.html", locals(), context_instance=RequestContext(request))

@login_required(login_url='/usuario/login/')
def musico(request):
    if request.user.is_authenticated():
        usuario_registrado=UsuarioRegistrado.objects.get(pk=request.user.id)
    return render_to_response("transferencia/musico.html", locals(), context_instance=RequestContext(request))

@login_required(login_url='/usuario/login/')
def complejo(request):
    if request.user.is_authenticated():
        usuario_registrado=UsuarioRegistrado.objects.get(pk=request.user.id)
    return render_to_response("transferencia/complejo.html", locals(), context_instance=RequestContext(request))

