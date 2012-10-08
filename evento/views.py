from django.template.context import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from usuario.models import UsuarioRegistrado
from evento.forms import EventoForm
from django.db.models import Q
from evento.models import Evento, AsistenciaFan, Participacion
from complejo.models import Complejo
from entrada.forms import ReservaEventoForm
from entrada.models import ReservaEvento,ConfiguracionEntradaEvento
from django.contrib.auth.decorators import login_required

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

def ver(request,evento_id):
    if request.user.is_authenticated():
        usuario_registrado=UsuarioRegistrado.objects.get(pk=request.user.id)
    evento=Evento.objects.get(pk=evento_id)
    cantidad_asistencia=AsistenciaFan.objects.filter(evento__id=evento_id, fan__id=request.user.id).count()
    cantidad_fan_asistir=AsistenciaFan.objects.filter(evento__id=evento_id).count()
    reservas_evento=ReservaEvento.objects.raw('Select re.* from RESERVA_EVENTO re JOIN CONFIGURACION_ENTRADA_EVENTO cee ON re.TIPO_ENTRADA_ID=cee.ID WHERE cee.EVENTO_ID=%s AND re.FAN_ID=%s',[evento_id, request.user.id])
    cantidad_reserva_entrada=len(list(reservas_evento))
    if cantidad_reserva_entrada == 1:
        reserva_evento=reservas_evento[0]
    form = ReservaEventoForm(evento_id)
    return render_to_response("evento/ver.html", locals(), context_instance=RequestContext(request))

@login_required(login_url='/usuario/login/')
def asistir(request,evento_id):
    asistencia=AsistenciaFan.objects.create(evento_id=evento_id, fan_id=request.user.id)
    asistencia.save()
    return HttpResponseRedirect(reverse('evento.views.ver', kwargs={'evento_id':evento_id}))

@login_required(login_url='/usuario/login/')
def no_asistir(request,evento_id):
    asistencia=AsistenciaFan.objects.filter(evento__id=evento_id, fan__id=request.user.id)
    asistencia.delete()
    return HttpResponseRedirect(reverse('evento.views.ver', kwargs={'evento_id':evento_id}))

	
	
	