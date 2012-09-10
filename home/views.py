# Create your views here.
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from usuario.models import UsuarioRegistrado
from noticia.models import NoticiaBanda, NoticiaComplejo, EstadoNoticia

def index(request):
    if request.user.is_authenticated():
        usuario_registrado=UsuarioRegistrado.objects.get(pk=request.user.id)
    noticias_banda=NoticiaBanda.objects.filter(estado=EstadoNoticia.objects.get(nombre="Publicado"))
    noticias_complejo=NoticiaComplejo.objects.filter(estado=EstadoNoticia.objects.get(nombre="Publicado"))
    return render_to_response("home/index.html", locals(), context_instance=RequestContext(request))
