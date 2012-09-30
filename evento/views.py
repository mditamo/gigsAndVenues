from django.template.context import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from usuario.models import UsuarioRegistrado
from evento.forms import EventoForm
from django.db.models import Q
from evento.models import Evento
from complejo.models import Complejo
from evento.models import Participacion


def evento_sin_negociacion(request):
    usuario_registrado=UsuarioRegistrado.objects.get(pk=request.user.id)
    if request.method == 'POST':
        form = EventoForm(request.POST)
        evento=form.save(commit=False)
        if form.is_valid():
            evento=form.save(commit=False)
            evento.complejo=Complejo.objects.get(pk=request.user.id)
            evento.save()
            for banda_id in request.POST.getlist('bandas'):
                participacion = Participacion.objects.create(evento_id=evento.id, banda_id=banda_id)
                participacion.estado="A confirmar"
                participacion.save()             
        return HttpResponseRedirect(reverse('evento.views.listado'))
    else:
        form = EventoForm()
        return render_to_response("evento/creacion_eventos.html", locals(), context_instance=RequestContext(request))

def listado(request):
    eventos=Evento.objects.filter(Q(complejo=request.user))
    eventos.query.order_by=['sede']
    usuario_registrado=UsuarioRegistrado.objects.get(pk=request.user.id)
    #sede=Sede.objects.get(pk=request)
    return render_to_response("evento/listado.html", locals(), context_instance=RequestContext(request))