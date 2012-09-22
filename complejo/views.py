# Create your views here.
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template.context import RequestContext
from complejo.models import *
from usuario.models import UsuarioRegistrado
from django.db.models import Q
from django.contrib.auth.decorators import login_required


def ver(request,complejo_id):
    return render_to_response("complejo/ver.html", locals(), context_instance=RequestContext(request))

@login_required(login_url='/usuario/login/')
def perfil(request):
    if request.user.is_authenticated():
        usuario_registrado=UsuarioRegistrado.objects.get(pk=request.user.id)
    complejo=Complejo.objects.get(pk=request.user.id)
    return render_to_response("complejo/perfil.html", locals(), context_instance=RequestContext(request))

@login_required(login_url='/usuario/login/')
def modificar(request,complejo_id):
        return render_to_response("complejo/modificar.html", locals(), context_instance=RequestContext(request))

@login_required(login_url='/usuario/login/')
def like(request,complejo_id):
    like_complejo = LikeComplejo.objects.create(banda_id=complejo_id, usuario_id=request.user.id)
    like_complejo.save()
    return HttpResponseRedirect(reverse('complejo.views.ver', kwargs={'complejo_id':complejo_id}))

@login_required(login_url='/usuario/login/')
def no_like(request,complejo_id):
    like_complejo=LikeComplejo.objects.filter(banda__id=complejo_id, usuario__id=request.user.id)
    like_complejo.delete()
    return HttpResponseRedirect(reverse('complejo.views.ver', kwargs={'complejo_id':complejo_id}))

@login_required(login_url='/usuario/login/')
def evento_sin_negociacion(request):
        return render_to_response("complejo/creacion_eventos.html", locals(), context_instance=RequestContext(request))
    
