# Create your views here.
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template.context import RequestContext
from usuario.models import UsuarioRegistrado 
from django.contrib.auth.decorators import login_required
from genero.models import Genero, LikeGenero
from suscripcion.models import SuscripcionGenero
from suscripcion.forms import SuscripcionGeneroForm
from banda.models import BandaGenero
from noticia.models import NoticiaBanda, EstadoNoticia


def ver(request,genero_id):
    if request.user.is_authenticated():
        usuario_registrado=UsuarioRegistrado.objects.get(pk=request.user.id)
    
    cantidad_suscripcion=SuscripcionGenero.objects.filter(genero__id=genero_id, usuario__id=request.user.id).count()
    form_suscripcion = SuscripcionGeneroForm()    
    genero=Genero.objects.get(pk=genero_id)
    bandas_genero=BandaGenero.objects.filter(genero__id=genero_id)
    cantidad_like=LikeGenero.objects.filter(genero__id=genero_id, usuario__id=request.user.id).count()
    cantidad_seguidores=LikeGenero.objects.filter(genero__id=genero_id).count()
    cantidad_suscripcion=SuscripcionGenero.objects.filter(genero__id=genero_id, usuario__id=request.user.id).count()
    estado_noticia=EstadoNoticia.objects.get(nombre="Publicado")
    noticias_genero=NoticiaBanda.objects.raw('Select nb.* from NOTICIA_BANDA nb join BANDA_GENERO bg ON nb.BANDA_ID=bg.BANDA_ID WHERE nb.ESTADO_ID=%s AND bg.GENERO_ID=%s',[estado_noticia.id, genero_id])
    cantidad_noticias_genero=len(list(noticias_genero))
    return render_to_response("genero/ver.html", locals(), context_instance=RequestContext(request))

@login_required(login_url='/usuario/login/')
def like(request,genero_id):
    like = LikeGenero.objects.create(genero_id=genero_id, usuario_id=request.user.id)
    like.save()
    return HttpResponseRedirect(reverse('genero.views.ver', kwargs={'genero_id':genero_id}))

@login_required(login_url='/usuario/login/')
def no_like(request,genero_id):
    like=LikeGenero.objects.filter(genero__id=genero_id, usuario__id=request.user.id)
    like.delete()
    return HttpResponseRedirect(reverse('genero.views.ver', kwargs={'genero_id':genero_id}))
        
@login_required(login_url='/usuario/login/')
def suscribirme(request,genero_id):
    form = SuscripcionGeneroForm(request.POST)
    suscripcion=form.save(commit=False)
    if form.is_valid():
        suscripcion.genero=Genero.objects.get(pk=genero_id)
        suscripcion.usuario=UsuarioRegistrado.objects.get(pk=request.user.id)
        suscripcion.save()
    return HttpResponseRedirect(reverse('genero.views.ver', kwargs={'genero_id':genero_id}))

@login_required(login_url='/usuario/login/')
def no_suscribirme(request,genero_id):
    suscripcion=SuscripcionGenero.objects.filter(genero__id=genero_id, usuario__id=request.user.id)
    suscripcion.delete()
    return HttpResponseRedirect(reverse('genero.views.ver', kwargs={'genero_id':genero_id}))
