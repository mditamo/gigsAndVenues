# Create your views here.
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template.context import RequestContext
from usuario.models import UsuarioRegistrado 
from multimedia.models import *
from multimedia.forms import *
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required(login_url='/usuario/login/')
def nuevo_recurso_multimedia_banda(request,banda_id):
    usuario_registrado=UsuarioRegistrado.objects.get(pk=request.user.id)
    
    banda=Banda.objects.get(pk=banda_id)
    if request.method == 'POST':
        form = RecursoMultimediaBandaForm(request.POST,request.FILES)
        if form.is_valid():
            recurso_multimedia_banda=form.save(commit=False)
            recurso_multimedia_banda.banda=banda
            recurso_multimedia_banda.save()
            messages.success(request, 'Se agrego correctamente el recurso multimedia')
            return HttpResponseRedirect(reverse('banda.views.administrar', kwargs={'banda_id':banda.id}))
    else:
        form = RecursoMultimediaBandaForm()
    return render_to_response("multimedia/nuevo_banda.html", locals(), context_instance=RequestContext(request))

@login_required(login_url='/usuario/login/')
def modificar_recurso_multimedia_banda(request,recurso_multimedia_id):
    usuario_registrado=UsuarioRegistrado.objects.get(pk=request.user.id)
    recurso_multimedia=RecursoMultimediaBanda.objects.get(pk=recurso_multimedia_id)
    if request.method == 'POST':
        form = RecursoMultimediaBandaForm(request.POST,request.FILES, instance=recurso_multimedia)
        if form.is_valid():
            recurso_multimedia.save()
            messages.success(request, 'Se modifico correctamente el recurso multimedia')
            return HttpResponseRedirect(reverse('banda.views.administrar', kwargs={'banda_id':recurso_multimedia.banda.id}))
    else:
        form = RecursoMultimediaBandaForm(instance=recurso_multimedia)
    return render_to_response("multimedia/modificar_banda.html", locals(), context_instance=RequestContext(request))

@login_required(login_url='/usuario/login/')
def eliminar_recurso_multimedia_banda(request,recurso_multimedia_id):
    recurso_multimedia=RecursoMultimediaBanda.objects.get(pk=recurso_multimedia_id)
    banda_id=recurso_multimedia.banda.id
    recurso_multimedia.delete()
    messages.success(request, 'Se borro correctamente el recurso multimedia')
    return HttpResponseRedirect(reverse('banda.views.administrar', kwargs={'banda_id':banda_id}))

@login_required(login_url='/usuario/login/')
def nuevo_recurso_multimedia_sede(request,sede_id):
    usuario_registrado=UsuarioRegistrado.objects.get(pk=request.user.id)
    sede=Sede.objects.get(pk=sede_id)
    if request.method == 'POST':
        form = RecursoMultimediaSedeForm(request.POST,request.FILES)
        if form.is_valid():
            recurso_multimedia_sede=form.save(commit=False)
            recurso_multimedia_sede.sede=sede
            recurso_multimedia_sede.save()
            messages.success(request, 'Se agrego correctamente el recurso multimedia')
            return HttpResponseRedirect(reverse('sede.views.administrar', kwargs={'sede_id':sede.id}))
    else:
        form = RecursoMultimediaSedeForm()
    return render_to_response("multimedia/nuevo_sede.html", locals(), context_instance=RequestContext(request))

@login_required(login_url='/usuario/login/')
def modificar_recurso_multimedia_sede(request,recurso_multimedia_id):
    usuario_registrado=UsuarioRegistrado.objects.get(pk=request.user.id)
    recurso_multimedia=RecursoMultimediaSede.objects.get(pk=recurso_multimedia_id)
    if request.method == 'POST':
        form = RecursoMultimediaSedeForm(request.POST,request.FILES, instance=recurso_multimedia)
        if form.is_valid():
            recurso_multimedia.save()
            messages.success(request, 'Se modifico correctamente el recurso multimedia')
            return HttpResponseRedirect(reverse('sede.views.administrar', kwargs={'sede_id':recurso_multimedia.sede.id}))
    else:
        form = RecursoMultimediaSedeForm(instance=recurso_multimedia)
    return render_to_response("multimedia/modificar_sede.html", locals(), context_instance=RequestContext(request))

@login_required(login_url='/usuario/login/')
def eliminar_recurso_multimedia_sede(request,recurso_multimedia_id):
    recurso_multimedia=RecursoMultimediaSede.objects.get(pk=recurso_multimedia_id)
    sede_id=recurso_multimedia.sede.id
    recurso_multimedia.delete()
    messages.success(request, 'Se borro correctamente el recurso multimedia')
    return HttpResponseRedirect(reverse('sede.views.administrar', kwargs={'sede_id':sede_id}))