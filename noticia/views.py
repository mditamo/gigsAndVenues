# Create your views here.
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template.context import RequestContext
from noticia.models import NoticiaBanda, EstadoNoticia, NoticiaComplejo
from noticia.forms import NoticiaBandaForm, NoticiaComplejoForm
from banda.models import Banda
from usuario.models import UsuarioRegistrado
from complejo.models import Complejo
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from itertools import chain

@login_required(login_url='/usuario/login/')
def nuevo_noticia_banda(request,banda_id):
    usuario_registrado=UsuarioRegistrado.objects.get(pk=request.user.id)
    banda=Banda.objects.get(pk=banda_id)
    if request.method == 'POST':
        form = NoticiaBandaForm(request.POST)
        if form.is_valid():
            noticia=form.save(commit=False)
            noticia.banda=banda
            noticia.fecha_publicacion=datetime.now().date()
            noticia.estado=EstadoNoticia.objects.get(nombre="Borrador")
            noticia.save()
            messages.success(request, 'Se agrego correctamente la noticia "%s".' % noticia.titulo)
            return HttpResponseRedirect(reverse('banda.views.administrar', kwargs={'banda_id':banda_id}))
    else:
        form= NoticiaBandaForm()
    return render_to_response("noticia/nuevo_noticia_banda.html", locals(), context_instance=RequestContext(request))

@login_required(login_url='/usuario/login/')
def publicar_noticia_banda(request,noticia_id):
    noticia=NoticiaBanda.objects.get(pk=noticia_id)
    noticia.estado=EstadoNoticia.objects.get(nombre="Publicado")
    noticia.save()
    messages.success(request, 'Se publico correctamente la noticia "%s".' % noticia.titulo)
    return HttpResponseRedirect(reverse('banda.views.administrar', kwargs={'banda_id':noticia.banda.id}))

@login_required(login_url='/usuario/login/')
def archivar_noticia_banda(request,noticia_id):
    noticia=NoticiaBanda.objects.get(pk=noticia_id)
    noticia.estado=EstadoNoticia.objects.get(nombre="Archivado")
    noticia.save()
    messages.success(request, 'Se archivo correctamente la noticia "%s".' % noticia.titulo)
    return HttpResponseRedirect(reverse('banda.views.administrar', kwargs={'banda_id':noticia.banda.id}))

@login_required(login_url='/usuario/login/')
def borrador_noticia_banda(request,noticia_id):
    noticia=NoticiaBanda.objects.get(pk=noticia_id)
    noticia.estado=EstadoNoticia.objects.get(nombre="Borrador")
    noticia.save()
    messages.success(request, 'Se paso a borrador correctamente la noticia "%s".' % noticia.titulo)
    return HttpResponseRedirect(reverse('banda.views.administrar', kwargs={'banda_id':noticia.banda.id}))

@login_required(login_url='/usuario/login/')
def eliminar_noticia_banda(request,noticia_id):
    noticia=NoticiaBanda.objects.get(pk=noticia_id)
    banda_id=noticia.banda.id
    titulo_noticia=noticia.titulo
    noticia.delete()
    messages.success(request, 'Se borro correctamente la noticia "%s".' % titulo_noticia )
    return HttpResponseRedirect(reverse('banda.views.administrar', kwargs={'banda_id':banda_id}))

def ver_noticia_banda(request,noticia_id):
    if request.user.is_authenticated():
        usuario_registrado=UsuarioRegistrado.objects.get(pk=request.user.id)
    noticia=NoticiaBanda.objects.get(pk=noticia_id)
    return render_to_response("noticia/ver.html", locals(), context_instance=RequestContext(request))


@login_required(login_url='/usuario/login/')
def modificar_noticia_banda(request,noticia_id):
    usuario_registrado=UsuarioRegistrado.objects.get(pk=request.user.id)
    noticia=NoticiaBanda.objects.get(pk=noticia_id)
    if request.method == 'POST':
        form = NoticiaBandaForm(request.POST, instance=noticia)
        if form.is_valid():
            form.save()
            messages.success(request, 'Se modifico correctamente la noticia "%s".' % noticia.titulo)
            return HttpResponseRedirect(reverse('banda.views.administrar', kwargs={'banda_id':noticia.banda.id}))
    else:
        form = NoticiaBandaForm(instance=noticia)
    return render_to_response("noticia/modificar_noticia_banda.html", locals(), context_instance=RequestContext(request))

@login_required(login_url='/usuario/login/')
def listado_noticia_complejo(request):
    noticias_complejo=NoticiaComplejo.objects.filter(complejo=request.user)
    usuario_registrado=UsuarioRegistrado.objects.get(pk=request.user.id)
    return render_to_response("noticia/listado_noticia_complejo.html", locals(), context_instance=RequestContext(request))    
    
@login_required(login_url='/usuario/login/')
def nuevo_noticia_complejo(request):
    usuario_registrado=UsuarioRegistrado.objects.get(pk=request.user.id)
    complejo=Complejo.objects.get(pk=request.user.id)
    if request.method == 'POST':
        form = NoticiaComplejoForm(request.POST)
        if form.is_valid():
            noticia=form.save(commit=False)
            noticia.complejo=complejo
            noticia.fecha_publicacion=datetime.now().date()
            noticia.estado=EstadoNoticia.objects.get(nombre="Borrador")
            noticia.save()
            messages.success(request, 'Se agrego correctamente la noticia "%s".' % noticia.titulo)
            return HttpResponseRedirect(reverse('noticia.views.listado_noticia_complejo', kwargs={}))
    else:
        form= NoticiaComplejoForm()
    return render_to_response("noticia/nuevo_noticia_complejo.html", locals(), context_instance=RequestContext(request))

@login_required(login_url='/usuario/login/')
def publicar_noticia_complejo(request,noticia_id):
    noticia=NoticiaComplejo.objects.get(pk=noticia_id)
    noticia.estado=EstadoNoticia.objects.get(nombre="Publicado")
    noticia.save()
    messages.success(request, 'Se publico correctamente la noticia "%s".' % noticia.titulo)
    return HttpResponseRedirect(reverse('noticia.views.listado_noticia_complejo', kwargs={}))

@login_required(login_url='/usuario/login/')
def archivar_noticia_complejo(request,noticia_id):
    noticia=NoticiaComplejo.objects.get(pk=noticia_id)
    noticia.estado=EstadoNoticia.objects.get(nombre="Archivado")
    noticia.save()
    messages.success(request, 'Se archivo correctamente la noticia "%s".' % noticia.titulo)
    return HttpResponseRedirect(reverse('noticia.views.listado_noticia_complejo', kwargs={}))

@login_required(login_url='/usuario/login/')
def borrador_noticia_complejo(request,noticia_id):
    noticia=NoticiaComplejo.objects.get(pk=noticia_id)
    noticia.estado=EstadoNoticia.objects.get(nombre="Borrador")
    noticia.save()
    messages.success(request, 'Se paso a borrador correctamente la noticia "%s".' % noticia.titulo)
    return HttpResponseRedirect(reverse('noticia.views.listado_noticia_complejo', kwargs={}))

@login_required(login_url='/usuario/login/')
def eliminar_noticia_complejo(request,noticia_id):
    noticia=NoticiaComplejo.objects.get(pk=noticia_id)
    titulo_noticia=noticia.titulo
    noticia.delete()
    messages.success(request, 'Se borro correctamente la noticia "%s".' % titulo_noticia )
    return HttpResponseRedirect(reverse('noticia.views.listado_noticia_complejo', kwargs={}))

@login_required(login_url='/usuario/login/')
def modificar_noticia_complejo(request,noticia_id):
    usuario_registrado=UsuarioRegistrado.objects.get(pk=request.user.id)
    noticia=NoticiaComplejo.objects.get(pk=noticia_id)
    if request.method == 'POST':
        form = NoticiaComplejoForm(request.POST, instance=noticia)
        if form.is_valid():
            form.save()
            messages.success(request, 'Se agrego correctamente la noticia "%s".' % noticia.titulo)
            return HttpResponseRedirect(reverse('noticia.views.listado_noticia_complejo', kwargs={}))
    else:
        form = NoticiaComplejoForm(instance=noticia)
    return render_to_response("noticia/modificar_noticia_complejo.html", locals(), context_instance=RequestContext(request))

def ver_noticia_complejo(request,noticia_id):
    if request.user.is_authenticated():
        usuario_registrado=UsuarioRegistrado.objects.get(pk=request.user.id)
    noticia=NoticiaComplejo.objects.get(pk=noticia_id)
    return render_to_response("noticia/ver.html", locals(), context_instance=RequestContext(request))


def listado(request):
    if request.user.is_authenticated():
        usuario_registrado=UsuarioRegistrado.objects.get(pk=request.user.id)
    
    noticias=NoticiaBanda.objects.filter(estado=EstadoNoticia.objects.get(nombre="Publicado"))
    noticias_complejo=NoticiaComplejo.objects.filter(estado=EstadoNoticia.objects.get(nombre="Publicado"))
    noticias=list(chain(noticias,noticias_complejo))
    paginator = Paginator(noticias, 3) # Show 25 contacts per page
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1
    try:
        noticias_banda = paginator.page(page)
    except (EmptyPage, InvalidPage):
        noticias_banda = paginator.page(paginator.num_pages)
    return render_to_response("noticia/listado.html", {"noticias_banda": noticias_banda})

