# Create your views here.
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template.context import RequestContext
from usuario.models import UsuarioRegistrado
from tema.forms import TemaBandaForm, TemaForm
from banda.models import Banda
from tema.models import TemaBanda

def nuevo(request,banda_id):
    usuario_registrado=UsuarioRegistrado.objects.get(pk=request.user.id)
    banda=Banda.objects.get(pk=banda_id)
    if request.method == 'POST':
        form_tema = TemaForm(request.POST)
        
        if form_tema.is_valid():
            tema=form_tema.save()
            tema_banda.banda=banda
            tema_banda.tema=tema
            tema_banda.save()
        return HttpResponseRedirect(reverse('banda.views.administrar', kwargs={'banda_id':banda_id}))
    else:
        form_tema= TemaForm()
        form= TemaBandaForm()
        return render_to_response("tema/nuevo.html", locals(), context_instance=RequestContext(request))

def modificar(request,tema_id,banda_id):
        usuario_registrado=UsuarioRegistrado.objects.get(pk=request.user.id)
        return render_to_response("tema/modificar.html", locals(), context_instance=RequestContext(request))

