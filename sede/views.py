# Create your views here.
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template.context import RequestContext
from usuario.models import UsuarioRegistrado
from sede.models import Sede, ConfiguracionSede
from sede.forms import SedeForm,ConfiguracionSedeForm
from direccion.forms import DireccionForm
from complejo.models import Complejo
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required(login_url='/usuario/login/')
def listado(request):
    if request.user.is_authenticated():
        usuario_registrado=UsuarioRegistrado.objects.get(pk=request.user.id)
    sedes=Sede.objects.filter(complejo__id=request.user.id)
    return render_to_response("sede/listado.html", locals(), context_instance=RequestContext(request))

@login_required(login_url='/usuario/login/')
def nuevo(request):
    usuario_registrado=UsuarioRegistrado.objects.get(pk=request.user.id)
    complejo=Complejo.objects.get(pk=request.user.id)
    if request.method == 'POST':
        form_dir = DireccionForm(request.POST)
        form = SedeForm(request.POST)
        if form.is_valid() and form_dir.is_valid():
            sede=form.save(commit=False)
            direccion=form_dir.save()
            sede.complejo=complejo
            sede.direccion=direccion
            sede.save()
            messages.success(request, 'Se agrego correctamente la sede "%s".' % sede.nombre)
            return HttpResponseRedirect(reverse('sede.views.listado'))
    else:
        form= SedeForm()
        form_dir = DireccionForm()
    return render_to_response("sede/nuevo.html", locals(), context_instance=RequestContext(request))

@login_required(login_url='/usuario/login/')
def modificar(request,sede_id):
    usuario_registrado=UsuarioRegistrado.objects.get(pk=request.user.id)
    sede=Sede.objects.get(pk=sede_id)
    if request.method == 'POST':
        form_dir = DireccionForm(request.POST, instance=sede.direccion)
        form = SedeForm(request.POST,instance=sede)
        if form.is_valid() and form_dir.is_valid():
            sede=form.save(commit=False)
            direccion=form_dir.save()
            sede.direccion=direccion
            sede.save()
            messages.success(request, 'Se modifico correctamente la sede "%s".' % sede.nombre)
            return HttpResponseRedirect(reverse('sede.views.listado'))
    else:
        form= SedeForm(instance=sede)
        form_dir = DireccionForm(instance=sede.direccion)
    return render_to_response("sede/modificar.html", locals(), context_instance=RequestContext(request))
   
@login_required(login_url='/usuario/login/')
def administrar(request,sede_id):
    usuario_registrado=UsuarioRegistrado.objects.get(pk=request.user.id)
    sede=Sede.objects.get(pk=sede_id)
    configuraciones_sede=ConfiguracionSede.objects.filter(sede__id=sede_id)
    return render_to_response("sede/administrar.html", locals(), context_instance=RequestContext(request))

@login_required(login_url='/usuario/login/')
def nueva_configuracion_sede(request,sede_id):
    usuario_registrado=UsuarioRegistrado.objects.get(pk=request.user.id)
    sede=Sede.objects.get(pk=sede_id)
    if request.method == 'POST':
        form = ConfiguracionSedeForm(request.POST)
        if form.is_valid():
            configuracion_sede=form.save(commit=False)
            configuracion_sede.sede=sede
            configuracion_sede.save()
            messages.success(request, 'Se agrego correctamente el esquema de entradas "%s".' % configuracion_sede.nombre)
            return HttpResponseRedirect(reverse('sede.views.administrar', kwargs={'sede_id':sede_id}))
    else:
        form= ConfiguracionSedeForm(instance=sede)
    return render_to_response("sede/nueva_configuracion_sede.html", locals(), context_instance=RequestContext(request))

@login_required(login_url='/usuario/login/')
def eliminar_configuracion_sede(request,configuracion_sede_id):
    configuracion_sede=ConfiguracionSede.objects.get(pk=configuracion_sede_id)
    sede_id=configuracion_sede.sede.id
    nombre_configuracion_sede=configuracion_sede.nombre
    configuracion_sede.delete()
    messages.success(request, 'Se borro correctamente el esquema de entradas "%s".' % nombre_configuracion_sede)
    return HttpResponseRedirect(reverse('sede.views.administrar', kwargs={'sede_id':sede_id}))


@login_required(login_url='/usuario/login/')
def modificar_configuracion_sede(request,configuracion_sede_id):
    usuario_registrado=UsuarioRegistrado.objects.get(pk=request.user.id)
    configuracion_sede=ConfiguracionSede.objects.get(pk=configuracion_sede_id)
    if request.method == 'POST':
        form = ConfiguracionSedeForm(request.POST, instance=configuracion_sede)
        if form.is_valid():
            configuracion_sede.save()
            messages.success(request, 'Se modifico correctamente el esquema de entradas "%s".' % configuracion_sede.nombre)
            return HttpResponseRedirect(reverse('sede.views.administrar', kwargs={'sede_id':configuracion_sede.sede.id}))
    else:
        form = ConfiguracionSedeForm(instance=configuracion_sede)
    return render_to_response("sede/modificar_configuracion_sede.html", locals(), context_instance=RequestContext(request))


