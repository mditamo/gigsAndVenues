# Create your views here.
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template.context import RequestContext
from banda.models import *
from disco.models import Disco
from musico.models import Musico
from usuario.models import UsuarioRegistrado
from banda.forms import *
from suscripcion.models import SuscripcionBanda
from suscripcion.forms import SuscripcionBandaForm
from noticia.models import NoticiaBanda, EstadoNoticia
from multimedia.models import RecursoMultimediaBanda
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required(login_url='/usuario/login/')
def listado(request):
    estado=EstadoComposicionBanda.objects.get(nombre="Confirmado")
    composiciones_banda=ComposicionBanda.objects.filter(Q(musico=request.user), Q(estado_id=estado))
    usuario_registrado=UsuarioRegistrado.objects.get(pk=request.user.id)
    return render_to_response("banda/listado.html", locals(), context_instance=RequestContext(request))

@login_required(login_url='/usuario/login/')
def solicitud(request):
    estado=EstadoComposicionBanda.objects.get(nombre="Solicitud")
    composiciones_banda=ComposicionBanda.objects.filter(Q(musico__id=request.user.id), Q(estado_id=estado))
    usuario_registrado=UsuarioRegistrado.objects.get(pk=request.user.id)
    return render_to_response("banda/solicitud.html", locals(), context_instance=RequestContext(request))

@login_required(login_url='/usuario/login/')
def confirmar_solicitud(request, banda_id):
    estado=EstadoComposicionBanda.objects.get(nombre="Confirmado")
    composicion_banda=ComposicionBanda.objects.get(musico__id=request.user.id, banda__id=banda_id)
    composicion_banda.estado=estado;
    composicion_banda.save();
    messages.success(request, 'El musico "%(nombre)s, %(apellido)s" confirmo correctamente la solicitud a la banda "%(banda)s" .'  % {'banda':composicion_banda.banda.nombre, 'nombre': composicion_banda.musico.first_name, 'apellido': composicion_banda.musico.last_name})
    return HttpResponseRedirect(reverse('banda.views.solicitud'))

@login_required(login_url='/usuario/login/')
def invitar_musico(request,banda_id):
    if request.user.is_authenticated():
        usuario_registrado=UsuarioRegistrado.objects.get(pk=request.user.id)
    banda=Banda.objects.get(pk=banda_id)
    musicos=Musico.objects.raw("select * from MUSICO m where m.USUARIOREGISTRADO_PTR_ID not in (select cb.musico_id from composicion_banda cb WHERE cb.banda_id=%s)",[banda_id])
    cantidad_musicos=len(list(musicos))
    return render_to_response("banda/invitar_musico.html", locals(), context_instance=RequestContext(request))

@login_required(login_url='/usuario/login/')
def enviar_invitacion(request,banda_id,musico_id):
    banda=Banda.objects.get(pk=banda_id)
    musico=Musico.objects.get(pk=musico_id)
    estado=EstadoComposicionBanda.objects.get(nombre="Solicitud")
    composicion_banda=ComposicionBanda(musico=musico,banda=banda,estado=estado)
    composicion_banda.save()
    messages.success(request, 'Se envio correctamente una invitacion al musico "%(nombre)s, %(apellido)s".' % {'nombre': musico.first_name, 'apellido': musico.last_name})
    return HttpResponseRedirect(reverse('banda.views.administrar', kwargs={'banda_id':banda_id}))

@login_required(login_url='/usuario/login/')
def administrar(request,banda_id):
    usuario_registrado=UsuarioRegistrado.objects.get(pk=request.user.id)
    banda=Banda.objects.get(pk=banda_id)
    generos_banda=BandaGenero.objects.filter(banda__id=banda_id)
    estado=EstadoComposicionBanda.objects.get(nombre="Solicitud")
    composiciones_banda=ComposicionBanda.objects.filter(Q(banda__id=banda_id), ~Q(estado_id=estado))
    discos=Disco.objects.filter(banda__id=banda_id)
    recursos_multimedia=RecursoMultimediaBanda.objects.filter(banda__id=banda_id)
    noticias_banda=NoticiaBanda.objects.filter(banda__id=banda_id)
    return render_to_response("banda/administrar.html", locals(), context_instance=RequestContext(request))

def ver(request,banda_id):
    if request.user.is_authenticated():
        usuario_registrado=UsuarioRegistrado.objects.get(pk=request.user.id)
    form_suscripcion = SuscripcionBandaForm()
    banda=Banda.objects.get(pk=banda_id)
    cantidad_like=LikeBanda.objects.filter(banda__id=banda_id, usuario__id=request.user.id).count()
    cantidad_seguidores=LikeBanda.objects.filter(banda__id=banda_id).count()
    
    suscripciones=SuscripcionBanda.objects.filter(banda__id=banda_id, usuario__id=request.user.id)
    if suscripciones.count() == 1:
        suscripcion=suscripciones[0]
    generos_banda=BandaGenero.objects.filter(banda__id=banda_id)
    estado=EstadoComposicionBanda.objects.get(nombre="Confirmado")
    composiciones_banda=ComposicionBanda.objects.filter(Q(banda__id=banda_id), Q(estado_id=estado))
    discos=Disco.objects.filter(banda__id=banda_id)
    estado_noticia=EstadoNoticia.objects.get(nombre="Publicado")
    noticias_banda=NoticiaBanda.objects.filter(Q(banda__id=banda_id), Q(estado_id=estado_noticia))
    recursos_multimedia=RecursoMultimediaBanda.objects.filter(banda__id=banda_id)
    return render_to_response("banda/ver.html", locals(), context_instance=RequestContext(request))

@login_required(login_url='/usuario/login/')
def confirmar(request,banda_id,musico_id):
    composicion_banda=ComposicionBanda.objects.get(banda__id=banda_id, musico__id=musico_id)
    composicion_banda.estado=EstadoComposicionBanda.objects.get(nombre="Confirmado")
    composicion_banda.save()
    messages.success(request, 'Se confirmo correctamente al integrante "%(nombre)s, %(apellido)s".' % {'nombre': composicion_banda.musico.first_name, 'apellido': composicion_banda.musico.last_name})
    return HttpResponseRedirect(reverse('banda.views.administrar', kwargs={'banda_id':banda_id}))

@login_required(login_url='/usuario/login/')
def denegar(request,banda_id,musico_id):
    composicion_banda=ComposicionBanda.objects.get(banda__id=banda_id, musico__id=musico_id)
    composicion_banda.estado=EstadoComposicionBanda.objects.get(nombre="Denegado")
    composicion_banda.save()
    messages.success(request, 'Se denego correctamente al integrante "%(nombre)s, %(apellido)s".' % {'nombre': composicion_banda.musico.first_name, 'apellido': composicion_banda.musico.last_name})
    return HttpResponseRedirect(reverse('banda.views.administrar', kwargs={'banda_id':banda_id}))

@login_required(login_url='/usuario/login/')
def eliminar(request,banda_id,musico_id):
    composicion_banda=ComposicionBanda.objects.get(banda__id=banda_id, musico__id=musico_id)
    composicion_banda.estado=EstadoComposicionBanda.objects.get(nombre="Eliminado")
    composicion_banda.save()
    messages.success(request, 'Se borro correctamente al integrante "%(nombre)s, %(apellido)s".' % {'nombre': composicion_banda.musico.first_name, 'apellido': composicion_banda.musico.last_name})
    return HttpResponseRedirect(reverse('banda.views.administrar', kwargs={'banda_id':banda_id}))

@login_required(login_url='/usuario/login/')
def modificar(request,banda_id):
    usuario_registrado=UsuarioRegistrado.objects.get(pk=request.user.id)
    banda=Banda.objects.get(pk=banda_id)
    if request.method == 'POST':
        form = BandaForm(request.POST,request.FILES, instance=banda)
        if form.is_valid():
            banda.generos.clear()
            for genero_id in request.POST.getlist('generos'):
                banda_genero = BandaGenero.objects.create(banda_id=banda_id, genero_id=genero_id)
                banda_genero.save()
            banda.save()
            messages.success(request, 'Se modifico correctamente la banda "%s".' % banda.nombre)
            return HttpResponseRedirect(reverse('banda.views.listado'))
    else:
        form = BandaForm(instance=banda)
    return render_to_response("banda/modificar.html", locals(), context_instance=RequestContext(request))

@login_required(login_url='/usuario/login/')
def nuevo(request):
    usuario_registrado=UsuarioRegistrado.objects.get(pk=request.user.id)
    musico=Musico.objects.get(pk=request.user.id)
    if request.method == 'POST':
        form = BandaForm(request.POST,request.FILES)
        if form.is_valid():
            banda=form.save(commit=False)
            banda.save()
            for genero_id in request.POST.getlist('generos'):
                banda_genero = BandaGenero.objects.create(banda_id=banda.id, genero_id=genero_id)
                banda_genero.save()
            estado=EstadoComposicionBanda.objects.get(nombre="Confirmado")
            composicion_banda=ComposicionBanda(musico_id=musico.id,banda_id=banda.id,estado=estado)
            composicion_banda.save()
            messages.success(request, 'Se agrego correctamente la banda "%(banda)s" y al musico "%(nombre)s, %(apellido)s" como integrante de la misma.' % {'banda': banda.nombre, 'nombre': composicion_banda.musico.first_name, 'apellido': composicion_banda.musico.last_name} )
            return HttpResponseRedirect(reverse('banda.views.listado'))
    else:
        form = BandaForm()
    return render_to_response("banda/nuevo.html", locals(), context_instance=RequestContext(request))

@login_required(login_url='/usuario/login/')
def modificar_composicion_banda(request,banda_id,musico_id):
    usuario_registrado=UsuarioRegistrado.objects.get(pk=request.user.id)
    composicion_banda=ComposicionBanda.objects.get(banda__id=banda_id, musico__id=musico_id)
    if request.method == 'POST':
        form = ComposicionBandaForm(request.POST, instance=composicion_banda)
        if form.is_valid():
            form.save()
            messages.success(request, 'Se modifico correctamente los datos integrante "%(nombre)s, %(apellido)s".' % {'nombre': composicion_banda.musico.first_name, 'apellido': composicion_banda.musico.last_name})
            return HttpResponseRedirect(reverse('banda.views.administrar', kwargs={'banda_id':banda_id}))
    else:
        form = ComposicionBandaForm(instance=composicion_banda)
    return render_to_response("banda/modificar_composicion_banda.html", locals(), context_instance=RequestContext(request))

@login_required(login_url='/usuario/login/')
def like(request,banda_id):
    like = LikeBanda.objects.create(banda_id=banda_id, usuario_id=request.user.id)
    like.save()
    return HttpResponseRedirect(reverse('banda.views.ver', kwargs={'banda_id':banda_id}))

@login_required(login_url='/usuario/login/')
def no_like(request,banda_id):
    like=LikeBanda.objects.filter(banda__id=banda_id, usuario__id=request.user.id)
    like.delete()
    return HttpResponseRedirect(reverse('banda.views.ver', kwargs={'banda_id':banda_id}))


@login_required(login_url='/usuario/login/')
def suscribirme(request,banda_id):
    form = SuscripcionBandaForm(request.POST)
    suscripcion=form.save(commit=False)
    if form.is_valid():
        suscripcion.banda=Banda.objects.get(pk=banda_id)
        suscripcion.usuario=UsuarioRegistrado.objects.get(pk=request.user.id)
        suscripcion.save()
    return HttpResponseRedirect(reverse('banda.views.ver', kwargs={'banda_id':banda_id}))

@login_required(login_url='/usuario/login/')
def no_suscribirme(request,banda_id):
    suscripcion=SuscripcionBanda.objects.filter(banda__id=banda_id, usuario__id=request.user.id)
    suscripcion.delete()
    return HttpResponseRedirect(reverse('banda.views.ver', kwargs={'banda_id':banda_id}))

