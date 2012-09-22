from django.template.context import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from usuario.models import UsuarioRegistrado
from evento.forms import EventoForm
from complejo.models import Sede

def evento_sin_negociacion(request):
    usuario_registrado=UsuarioRegistrado.objects.get(pk=request.user.id)
    sede=Sede.objects.get(pk=request.user.id)
    if request.method == 'POST':
        form = EventoForm(request.POST)
        evento=form.save(commit=False)
        if form.is_valid():
            evento.save()
            #estado=EstadoComposicionBanda.objects.get(nombre="Confirmado")
   
        return HttpResponseRedirect(reverse('evento.views.listado'))
    else:
        form = EventoForm()
        return render_to_response("evento/creacion_eventos.html", locals(), context_instance=RequestContext(request))
