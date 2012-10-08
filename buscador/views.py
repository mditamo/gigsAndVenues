# Create your views here.
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from usuario.models import UsuarioRegistrado
from genero.models import Genero
from banda.models import Banda
from musico.models import Musico
from complejo.models import Complejo
from fan.models import Fan
    
def index(request):
    if request.user.is_authenticated():
        usuario_registrado=UsuarioRegistrado.objects.get(pk=request.user.id)
    if request.method == 'POST' and request.POST['nombre']!="":
        generos=Genero.objects.filter(nombre=request.POST['nombre'])
        cantidad_generos=generos.count()
        bandas=Banda.objects.filter(nombre=request.POST['nombre'])
        cantidad_bandas=bandas.count()
        musicos=Musico.objects.filter(username=request.POST['nombre'])
        cantidad_musicos=musicos.count()
        complejos=Complejo.objects.filter(nombre=request.POST['nombre'])
        cantidad_complejos=complejos.count()
        fans=Fan.objects.filter(username=request.POST['nombre'])
        cantidad_fans=fans.count()
    else:
        cantidad_fans=0
        cantidad_musicos=0
        cantidad_complejos=0
        cantidad_bandas=0
        cantidad_generos=0
    return render_to_response("buscador/index.html", locals(), context_instance=RequestContext(request))

