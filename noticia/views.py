# Create your views here.
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template.context import RequestContext
from noticia.models import NoticiaBanda, EstadoNoticia
from noticia.forms import NoticiaBandaForm
from banda.models import Banda
from usuario.models import UsuarioRegistrado
from datetime import datetime

def nuevo_noticia_banda(request,banda_id):
    usuario_registrado=UsuarioRegistrado.objects.get(pk=request.user.id)
    banda=Banda.objects.get(pk=banda_id)
    if request.method == 'POST':
        form = NoticiaBandaForm(request.POST)
        noticia=form.save(commit=False)
        if form.is_valid():
            noticia.banda=banda
            noticia.fecha_publicacion=datetime.now().date()
            noticia.estado=EstadoNoticia.objects.get(nombre="Borrador")
            noticia.save()
        return HttpResponseRedirect(reverse('banda.views.administrar', kwargs={'banda_id':banda_id}))
    else:
        form= NoticiaBandaForm()
        return render_to_response("noticia/nuevo_noticia_banda.html", locals(), context_instance=RequestContext(request))

def publicar_noticia_banda(request,noticia_id):
    noticia=NoticiaBanda.objects.get(pk=noticia_id)
    noticia.estado=EstadoNoticia.objects.get(nombre="Publicado")
    noticia.save()
    return HttpResponseRedirect(reverse('banda.views.administrar', kwargs={'banda_id':noticia.banda.id}))

def archivar_noticia_banda(request,noticia_id):
    noticia=NoticiaBanda.objects.get(pk=noticia_id)
    noticia.estado=EstadoNoticia.objects.get(nombre="Archivado")
    noticia.save()
    return HttpResponseRedirect(reverse('banda.views.ver', kwargs={'banda_id':noticia.banda.id}))

def borrador_noticia_banda(request,noticia_id):
    noticia=NoticiaBanda.objects.get(pk=noticia_id)
    noticia.estado=EstadoNoticia.objects.get(nombre="Borrador")
    noticia.save()
    return HttpResponseRedirect(reverse('banda.views.administrar', kwargs={'banda_id':noticia.banda.id}))

def eliminar_noticia_banda(request,noticia_id):
    noticia=NoticiaBanda.objects.get(pk=noticia_id)
    banda_id=noticia.banda.id
    noticia.delete()
    return HttpResponseRedirect(reverse('banda.views.administrar', kwargs={'banda_id':banda_id}))

def detalle_noticia_banda(request,noticia_id):
    usuario_registrado=UsuarioRegistrado.objects.get(pk=request.user.id)
    noticia=NoticiaBanda.objects.get(pk=noticia_id)
    return render_to_response("noticia/detalle_noticia_banda.html", locals(), context_instance=RequestContext(request))

def modificar_noticia_banda(request,noticia_id):
    usuario_registrado=UsuarioRegistrado.objects.get(pk=request.user.id)
    noticia=NoticiaBanda.objects.get(pk=noticia_id)
    if request.method == 'POST':
        form = NoticiaBandaForm(request.POST, instance=noticia)
        form.save()
        return HttpResponseRedirect(reverse('banda.views.administrar', kwargs={'banda_id':noticia.banda.id}))
    else:
        form = NoticiaBandaForm(instance=noticia)
        return render_to_response("noticia/modificar_noticia_banda.html", locals(), context_instance=RequestContext(request))