# Create your views here.
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template.context import RequestContext
from complejo.models import *
from complejo.forms import *
from suscripcion.models import SuscripcionComplejo
from suscripcion.forms import SuscripcionComplejoForm
from usuario.models import UsuarioRegistrado
from django.db.models import Q
from direccion.forms import DireccionForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def ver(request,complejo_id):
    if request.user.is_authenticated():
        usuario_registrado=UsuarioRegistrado.objects.get(pk=request.user.id)
    complejo=Complejo.objects.get(pk=complejo_id)
    cantidad_like=LikeComplejo.objects.filter(complejo__id=complejo_id, usuario__id=request.user.id).count()
    cantidad_seguidores=LikeComplejo.objects.filter(complejo__id=complejo_id).count()
    cantidad_suscripcion=SuscripcionComplejo.objects.filter(complejo__id=complejo_id, usuario__id=request.user.id).count()
    form_suscripcion = SuscripcionComplejoForm()    
    return render_to_response("complejo/ver.html", locals(), context_instance=RequestContext(request))

@login_required(login_url='/usuario/login/')
def perfil(request):
    if request.user.is_authenticated():
        usuario_registrado=UsuarioRegistrado.objects.get(pk=request.user.id)
    complejo=Complejo.objects.get(pk=request.user.id)
    return render_to_response("complejo/perfil.html", locals(), context_instance=RequestContext(request))

@login_required(login_url='/usuario/login/')
def modificar(request,complejo_id):
    if request.user.is_authenticated():
        usuario_registrado=UsuarioRegistrado.objects.get(pk=request.user.id)
    complejo=Complejo.objects.get(pk=complejo_id)
    if request.method == 'POST':
        form_dir = DireccionForm(request.POST)
        form = ComplejoForm(request.POST, instance=complejo)
        if form.is_valid() and form_dir.is_valid():
            complejo=form.save(commit=False)
            direccion=form_dir.save()
            complejo.direccion=direccion
            complejo.save()
            messages.success(request, 'Se modifico correctamente los datos del complejo "%s".' % complejo.nombre)
            return render_to_response("complejo/perfil.html", locals(), context_instance=RequestContext(request))
    else:
        form = ComplejoForm(instance=complejo)
        form_dir = DireccionForm(instance=complejo.direccion)
    return render_to_response("complejo/modificar.html", locals(), context_instance=RequestContext(request))

@login_required(login_url='/usuario/login/')
def like(request,complejo_id):
    like = LikeComplejo.objects.create(banda_id=complejo_id, usuario_id=request.user.id)
    like.save()
    return HttpResponseRedirect(reverse('complejo.views.ver', kwargs={'complejo_id':complejo_id}))

@login_required(login_url='/usuario/login/')
def no_like(request,complejo_id):
    like=LikeComplejo.objects.filter(banda__id=complejo_id, usuario__id=request.user.id)
    like.delete()
    return HttpResponseRedirect(reverse('complejo.views.ver', kwargs={'complejo_id':complejo_id}))

@login_required(login_url='/usuario/login/')
def suscribirme(request,complejo_id):
    form = SuscripcionComplejoForm(request.POST)
    suscripcion=form.save(commit=False)
    if form.is_valid():
        suscripcion.complejo=Complejo.objects.get(pk=complejo_id)
        suscripcion.usuario=UsuarioRegistrado.objects.get(pk=request.user.id)
        suscripcion.save()
    return HttpResponseRedirect(reverse('complejo.views.ver', kwargs={'complejo_id':complejo_id}))

@login_required(login_url='/usuario/login/')
def no_suscribirme(request,complejo_id):
    suscripcion=SuscripcionComplejo.objects.filter(complejo__id=complejo_id, usuario__id=request.user.id)
    suscripcion.delete()
    return HttpResponseRedirect(reverse('complejo.views.ver', kwargs={'complejo_id':complejo_id}))


@login_required(login_url='/usuario/login/')
def evento_sin_negociacion(request):
        return render_to_response("complejo/creacion_eventos.html", locals(), context_instance=RequestContext(request))
    
