# Create your views here.
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from usuario.models import UsuarioRegistrado
from noticia.models import NoticiaBanda, NoticiaComplejo, EstadoNoticia
from evento.models import Evento

def noticia_listado(request):
    if request.user.is_authenticated() and not(request.user.is_superuser):
        usuario_registrado=UsuarioRegistrado.objects.get(pk=request.user.id)
    noticias_banda=NoticiaBanda.objects.filter(estado=EstadoNoticia.objects.get(nombre="Publicado"))
    noticias_complejo=NoticiaComplejo.objects.filter(estado=EstadoNoticia.objects.get(nombre="Publicado"))
    return render_to_response("celular/noticia_listado.html", locals(), context_instance=RequestContext(request))

def evento_listado(request):
    if request.user.is_authenticated() and not(request.user.is_superuser):
        usuario_registrado=UsuarioRegistrado.objects.get(pk=request.user.id)
    eventos=Evento.objects.all()
    eventos.query.order_by=['fecha']
    return render_to_response("celular/evento_listado.html", locals(), context_instance=RequestContext(request))

def usuario_login(request):
    return render_to_response("celular/usuario_login.html", locals(), context_instance=RequestContext(request))

def ver_noticia_complejo(request,noticia_id):
    if request.user.is_authenticated():
        usuario_registrado=UsuarioRegistrado.objects.get(pk=request.user.id)
    noticia=NoticiaComplejo.objects.get(pk=noticia_id)
    return render_to_response("celular/ver_noticia.html", locals(), context_instance=RequestContext(request))


def ver_noticia_banda(request,noticia_id):
    if request.user.is_authenticated():
        usuario_registrado=UsuarioRegistrado.objects.get(pk=request.user.id)
    noticia=NoticiaBanda.objects.get(pk=noticia_id)
    return render_to_response("celular/ver_noticia.html", locals(), context_instance=RequestContext(request))