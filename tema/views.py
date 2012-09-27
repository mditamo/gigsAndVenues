# Create your views here.
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template.context import RequestContext
from usuario.models import UsuarioRegistrado
from tema.forms import TemaBandaForm, TemaForm
from banda.models import Banda
from tema.models import TemaBanda
from disco.models import ComposicionDisco
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required(login_url='/usuario/login/')
def nuevo(request,banda_id):
    usuario_registrado=UsuarioRegistrado.objects.get(pk=request.user.id)
    banda=Banda.objects.get(pk=banda_id)
    if request.method == 'POST':
        form_tema = TemaForm(request.POST)
        form = TemaBandaForm(request.POST)
        if form_tema.is_valid():
            tema_banda=form.save(commit=False)
            tema=form_tema.save()
            tema_banda.banda=banda
            tema_banda.tema=tema
            tema_banda.save()
            messages.success(request, 'Se agrego correctamente el tema "%s".' % tema.nombre)
            return HttpResponseRedirect(reverse('banda.views.administrar', kwargs={'banda_id':banda_id}))
    else:
        form_tema= TemaForm()
        form= TemaBandaForm()
    return render_to_response("tema/nuevo.html", locals(), context_instance=RequestContext(request))

@login_required(login_url='/usuario/login/')
def modificar(request,tema_id,banda_id):
    usuario_registrado=UsuarioRegistrado.objects.get(pk=request.user.id)
    tema_banda=TemaBanda.objects.get(tema__id=tema_id, banda__id=banda_id)
    if request.method == 'POST':
        form_tema = TemaForm(request.POST, instance=tema_banda.tema)
        form = TemaBandaForm(request.POST,instance=tema_banda)
        if form.is_valid():
            tema_banda=form.save(commit=False)
            tema=form_tema.save()
            tema_banda.tema=tema
            tema_banda.save()
            messages.success(request, 'Se modifico correctamente el tema "%s".' % tema.nombre)
            return HttpResponseRedirect(reverse('banda.views.administrar', kwargs={'banda_id':banda_id}))
    else:
        form= TemaBandaForm(instance=tema_banda)
        form_tema = TemaForm(instance=tema_banda.tema)
    return render_to_response("tema/modificar.html", locals(), context_instance=RequestContext(request))

@login_required(login_url='/usuario/login/')
def eliminar(request,tema_id,banda_id):
    tema_banda=TemaBanda.objects.get(tema__id=tema_id, banda__id=banda_id)
    cantidad_composiciones_disco=ComposicionDisco.objects.filter(tema_banda__id=tema_banda.id).count()
    if cantidad_composiciones_disco > 0:
        messages.error(request, 'NO se puede borrar el tema por que pertenece a algun disco')
    else:
        nombre_tema=tema_banda.tema.nombre
        tema_banda.delete()
        messages.success(request, 'Se borro correctamente el tema "%s".' % nombre_tema)
    return HttpResponseRedirect(reverse('banda.views.administrar', kwargs={'banda_id':banda_id}))
    
