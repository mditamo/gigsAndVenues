# Create your views here.
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template.context import RequestContext
from usuario.models import UsuarioRegistrado 
from django.contrib.auth.decorators import login_required
from genero.models import Genero, LikeGenero
from banda.models import BandaGenero
from noticia.models import NoticiaBanda


def ver(request,genero_id):
    if request.user.is_authenticated():
        usuario_registrado=UsuarioRegistrado.objects.get(pk=request.user.id)
    genero=Genero.objects.get(pk=genero_id)
    bandas_genero=BandaGenero.objects.filter(genero__id=genero_id)
    cantidad_like=LikeGenero.objects.filter(genero__id=genero_id, usuario__id=request.user.id).count()
    cantidad_seguidores=LikeGenero.objects.filter(genero__id=genero_id).count()
    noticias=NoticiaBanda.objects.raw('Select nb.* from NOTICIA_BANDA nb join BANDA_GENERO bg ON nb.BANDA_ID=bg.BANDA_ID WHERE bg.GENERO_ID=%s',[genero_id])
    return render_to_response("genero/ver.html", locals(), context_instance=RequestContext(request))

@login_required(login_url='/usuario/login/')
def like(request,genero_id):
    like_genero = LikeGenero.objects.create(genero_id=genero_id, usuario_id=request.user.id)
    like_genero.save()
    return HttpResponseRedirect(reverse('genero.views.ver', kwargs={'genero_id':genero_id}))

@login_required(login_url='/usuario/login/')
def no_like(request,genero_id):
    like_genero=LikeGenero.objects.filter(genero__id=genero_id, usuario__id=request.user.id)
    like_genero.delete()
    return HttpResponseRedirect(reverse('genero.views.ver', kwargs={'genero_id':genero_id}))
        
        
    