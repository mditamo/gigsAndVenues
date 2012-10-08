from django.template.context import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from usuario.models import UsuarioRegistrado
from django.db.models import Q
from entrada.models import ReservaEvento, EstadoReserva, ConfiguracionEntradaEvento
from entrada.forms import ReservaEventoForm, ConfiguracionEntradaEventoForm
from evento.models import Evento
from sede.models import ConfiguracionSede
from fan.models import Fan
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from datetime import datetime

@login_required(login_url='/usuario/login/')
def retiro_entrada_index(request):
    usuario_registrado=UsuarioRegistrado.objects.get(pk=request.user.id)
    usuario_id=request.user.id
    estado_reserva=EstadoReserva.objects.get(nombre="Pendiente")
    if request.method == 'POST' and request.POST['codigo_retiro']!="":
        reservas_evento=ReservaEvento.objects.filter(codigo_retiro=request.POST['codigo_retiro'])
        cantidad_reservas_evento_buscador=reservas_evento.count()
    else:
        reservas_evento=ReservaEvento.objects.raw('Select re.* from RESERVA_EVENTO re JOIN CONFIGURACION_ENTRADA_EVENTO cee ON re.TIPO_ENTRADA_ID=cee.ID JOIN EVENTO e ON cee.EVENTO_ID=e.ID WHERE e.COMPLEJO_ID=%s AND re.ESTADO_ID=%s',[usuario_id, estado_reserva.id])
        cantidad_reservas_evento=len(list(reservas_evento))
    return render_to_response("entrada/retiro_entrada_index.html", locals(), context_instance=RequestContext(request))


@login_required(login_url='/usuario/login/')
def confirmar_retiro_entrada(request,reserva_entrada_id):
    usuario_registrado=UsuarioRegistrado.objects.get(pk=request.user.id)
    reserva_evento=ReservaEvento.objects.get(pk=reserva_entrada_id)
    reserva_evento.estado=EstadoReserva.objects.get(nombre="Confirmado")
    reserva_evento.save();
    messages.success(request, 'La reserva con codigo "%(codigo_retiro)s para el evento %(nombre_evento)s" fue confirmada con exito" .'  % {'codigo_retiro':reserva_evento.codigo_retiro, 'nombre_evento': reserva_evento.tipo_entrada.evento.nombre})
    return HttpResponseRedirect(reverse('entrada.views.retiro_entrada_index'))


@login_required(login_url='/usuario/login/')
def reservar_entrada(request,evento_id):
    if request.method == 'POST':
        form = ReservaEventoForm(evento_id,request.POST)
        if form.is_valid():
            reserva=form.save(commit=False)
            reserva.fan=Fan.objects.get(pk=request.user.id)
            reserva.codigo_retiro=123456
            reserva.fecha_vencimiento=datetime.now().date()
            reserva.estado=EstadoReserva.objects.get(nombre="Pendiente")
            reserva.save()
            return HttpResponseRedirect(reverse('evento.views.ver', kwargs={'evento_id':evento_id}))
    
    
@login_required(login_url='/usuario/login/')
def eliminar_reserva_entrada(request,evento_id):
    reservas_evento=ReservaEvento.objects.raw('Select re.* from RESERVA_EVENTO re JOIN CONFIGURACION_ENTRADA_EVENTO cee ON re.TIPO_ENTRADA_ID=cee.ID WHERE cee.EVENTO_ID=%s AND re.FAN_ID=%s',[evento_id, request.user.id])
    for reserva_evento in reservas_evento:
        reserva_evento.delete()
        codigo_retiro=reserva_evento.codigo_retiro
        nombre_evento=reserva_evento.tipo_entrada.evento.nombre
        messages.success(request, 'La reserva con codigo "%(codigo_retiro)s para el evento %(nombre_evento)s" fue eliminada con exito" .'  % {'codigo_retiro': codigo_retiro, 'nombre_evento': nombre_evento})    
    return HttpResponseRedirect(reverse('entrada.views.listado'))


@login_required(login_url='/usuario/login/')
def entrada_listado(request):
    usuario_registrado=UsuarioRegistrado.objects.get(pk=request.user.id)
    reservas_evento=ReservaEvento.objects.filter(fan__id=request.user.id)
    return render_to_response("entrada/listado.html", locals(), context_instance=RequestContext(request))

@login_required(login_url='/usuario/login/')
def seleccionar_configuracion_sede(request, evento_id, sede_id):
    usuario_registrado=UsuarioRegistrado.objects.get(pk=request.user.id)
    configuraciones_sede=ConfiguracionSede.objects.filter(sede__id=sede_id)
    return render_to_response("entrada/seleccionar_configuracion_sede.html", locals(), context_instance=RequestContext(request))

@login_required(login_url='/usuario/login/')
def listado_esquema_entrada(request,sede_id, evento_id):
    usuario_registrado=UsuarioRegistrado.objects.get(pk=request.user.id)
    configuraciones_esquema_entrada=ConfiguracionEntradaEvento.objects.filter(evento__id=evento_id)
    return render_to_response("entrada/listado_esquema_reserva.html", locals(), context_instance=RequestContext(request))

@login_required(login_url='/usuario/login/')
def nuevo_esquema_entrada(request, evento_id, sede_id, configuracion_sede_id):
    usuario_registrado=UsuarioRegistrado.objects.get(pk=request.user.id)
    configuracion_sede=ConfiguracionSede.objects.get(pk=configuracion_sede_id)
    evento=Evento.objects.get(pk=evento_id)
    if request.method == 'POST':
        form = ConfiguracionEntradaEventoForm(request.POST)
        if form.is_valid():
            configuracion_entrada_evento=form.save(commit=False)
            configuracion_entrada_evento.evento=evento
            configuracion_entrada_evento.cantidad_entradas_disponibles=configuracion_sede.cantidad_entradas_disponibles
            configuracion_entrada_evento.cantidad_entradas_reserva=configuracion_sede.cantidad_entradas_reserva
            configuracion_entrada_evento.save()
            messages.success(request, 'Se agrego correctamente el esquema de entradas "%(nombre_esquema)s" para el evento "%(nombre_evento)s"' % {'nombre_esquema': configuracion_sede.nombre, 'nombre_evento': evento.nombre} )
            return HttpResponseRedirect(reverse('entrada.views.listado_esquema_entrada', kwargs={'evento_id':evento.id, 'sede_id':sede_id}))
    else:
        form = ConfiguracionEntradaEventoForm()
    return render_to_response("entrada/nuevo_esquema_entrada.html", locals(), context_instance=RequestContext(request))

@login_required(login_url='/usuario/login/')
def modificar_esquema_entrada(request, configuracion_esquema_entrada_id):
    usuario_registrado=UsuarioRegistrado.objects.get(pk=request.user.id)
    configuracion_esquema_entrada=ConfiguracionEntradaEvento.objects.get(pk=configuracion_esquema_entrada_id)
    if request.method == 'POST':
        form = ConfiguracionEntradaEventoForm(request.POST, instance=configuracion_esquema_entrada)
        if form.is_valid():
            configuracion_esquema_entrada.save()
            messages.success(request, 'Se modifico correctamente el esquema de entradas "%(nombre_esquema)s" para el evento "%(nombre_evento)s"' % {'nombre_esquema': configuracion_esquema_entrada.nombre, 'nombre_evento': configuracion_esquema_entrada.evento.nombre} )
            return HttpResponseRedirect(reverse('entrada.views.listado_esquema_entrada', kwargs={'evento_id':configuracion_esquema_entrada.evento.id,'sede_id':configuracion_esquema_entrada.evento.sede.id}))
    else:
        form = ConfiguracionEntradaEventoForm(instance=configuracion_esquema_entrada)
    return render_to_response("entrada/modificar_esquema_entrada.html", locals(), context_instance=RequestContext(request))

@login_required(login_url='/usuario/login/') 
def eliminar_esquema_entrada(request, configuracion_esquema_entrada_id):
    configuracion_esquema_entrada=ConfiguracionEntradaEvento.objects.get(pk=configuracion_esquema_entrada_id)
    evento_id=configuracion_esquema_entrada.evento.id
    sede_id=configuracion_esquema_entrada.evento.sede.id
    nombre_evento=configuracion_esquema_entrada.evento.nombre
    nombre_esquema_entrada=configuracion_esquema_entrada.nombre
    configuracion_esquema_entrada.delete()
    messages.success(request, 'Se borro correctamente el esquema de entradas "%(nombre_esquema)s" para el evento "%(nombre_evento)s"' % {'nombre_esquema': nombre_esquema_entrada, 'nombre_evento': nombre_evento} )
    return HttpResponseRedirect(reverse('entrada.views.listado_esquema_entrada', kwargs={'evento_id':evento_id,'sede_id':sede_id}))