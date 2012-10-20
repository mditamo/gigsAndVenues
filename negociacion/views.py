from django.template.context import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from usuario.models import UsuarioRegistrado
from negociacion.forms import NegociacionComplejoFormPaso1,NegociacionBandaFormPaso1
from negociacion.forms import NegociacionComplejoFormPaso2,NegociacionBandaFormPaso2
from negociacion.forms import NegociacionComplejoFormPaso3,NegociacionBandaFormPaso3
from negociacion.models import NegociacionBanda,CondicionNegociacion, EstadoNegociacion
from django.db.models import Q
from negociacion.models import Negociacion
from condiciones.forms import CondicionUnitariaForm
from banda.models import Banda, ComposicionBanda
from django.contrib import messages
from evento.models import Evento,Participacion
from sede.models import Sede

def negociacionPaso1(request):
    usuario_registrado=UsuarioRegistrado.objects.get(pk=request.user.id)
    if request.method == 'POST':   
        if usuario_registrado.is_complejo():
            form = NegociacionComplejoFormPaso1(request.POST)
            negociacion=form.save(commit=False)
            negociacion.inicio_negociacion = "C"
            negociacion.complejo_id=request.user.id
        else:
            form = NegociacionBandaFormPaso1(request.POST)
            negociacion=form.save(commit=False)
            negociacion.inicio_negociacion = "B"
            
        negociacion.estado=EstadoNegociacion.objects.get(nombre="Pendiente")
        if form.is_valid():
            negociacion.save()
        return HttpResponseRedirect(reverse('negociacion.views.negociacionPaso2', kwargs={'negociacion_id':negociacion.id}))
    else:
        if usuario_registrado.is_complejo():
            form = NegociacionComplejoFormPaso1()
            form.fields['sede'].queryset=Sede.objects.filter(complejo_id=request.user.id)
        else:
            form = NegociacionBandaFormPaso1()
        return render_to_response("negociacion/nuevo.html", locals(), context_instance=RequestContext(request))

def negociacionPaso2(request,negociacion_id):
    usuario_registrado=UsuarioRegistrado.objects.get(pk=request.user.id)
    if request.method == 'POST':
        if usuario_registrado.is_complejo():
            form = NegociacionComplejoFormPaso2(request.POST)       
        else:
            form = NegociacionBandaFormPaso2(request.POST)        
        negociacion=form.save(commit=False)
        estadoBanda=EstadoNegociacion.objects.get(nombre="Pendiente") 
        negociacionTratada=Negociacion.objects.get(pk=negociacion_id)     
        if form.is_valid():
            if negociacionTratada.inicio_negociacion=="C" :
                for banda_id in request.POST.getlist('bandas'):
                    negociacionBanda = NegociacionBanda.objects.create(negociacion_id=negociacion_id, banda_id=banda_id,estado=estadoBanda)
                    negociacionBanda.save()
            else:
                negociacionTratada.banda_id=negociacion.banda_id
                negociacionTratada.sede_id=negociacion.sede_id
                negociacionTratada.save();
                negociacionBanda = NegociacionBanda.objects.create(negociacion_id=negociacion_id, banda_id=negociacion.banda_id,estado=estadoBanda)
        return HttpResponseRedirect(reverse('negociacion.views.negociacionPaso3', kwargs={'negociacion_id':negociacion_id}))
    else:
        if usuario_registrado.is_complejo():
            form = NegociacionComplejoFormPaso2()
        else:
            bandasMusico=Banda.objects.filter(composicionbanda__musico=request.user.id)
            negociacion=Negociacion.objects.get(pk=negociacion_id)
            form = NegociacionBandaFormPaso2()
            form.fields['banda'].queryset=bandasMusico     
            form.fields['sede'].queryset=Sede.objects.filter(complejo_id=negociacion.complejo)
            

        return render_to_response("negociacion/nuevo2.html", locals(), context_instance=RequestContext(request))
    
def negociacionPaso3(request,negociacion_id):
    usuario_registrado=UsuarioRegistrado.objects.get(pk=request.user.id)
    if request.method == 'POST':
        if usuario_registrado.is_complejo():
            form = NegociacionComplejoFormPaso3(request.POST)       
        else:
            form = NegociacionBandaFormPaso3(request.POST)        
        negociacion=form.save(commit=False)      
        if form.is_valid():
            negociacionTratada = Negociacion.objects.get(pk=negociacion_id)
            negociacionTratada.fecha=negociacion.fecha 
            negociacionTratada.hora=negociacion.hora 
            negociacionTratada.save()
        #return HttpResponseRedirect(reverse('negociacion.views.listado'))
        #return HttpResponseRedirect(reverse('negociacion.views.negociacionPaso4', kwargs={'negociacion_id':negociacion_id}))
        return HttpResponseRedirect(reverse('condiciones.views.agregarCondicion', kwargs={'negociacion_id':negociacion_id}))
    else:
        if usuario_registrado.is_complejo():
            form = NegociacionComplejoFormPaso3()
        else:
            form = NegociacionBandaFormPaso3()
        return render_to_response("negociacion/nuevo3.html", locals(), context_instance=RequestContext(request))

def negociacionPaso4(request,negociacion_id):
    usuario_registrado=UsuarioRegistrado.objects.get(pk=request.user.id)
    if request.method == 'POST':
        form = CondicionUnitariaForm(request.POST)              
        condicion=form.save(commit=False)      
        if form.is_valid():
            condicionNegociacion = CondicionNegociacion.objects.create(negociacion_id=negociacion_id, condicionUnitaria_id=request.user.id)
            condicionNegociacion.save()
            condicion.save
        return HttpResponseRedirect(reverse('negociacion.views.listado'))
    else:
        form = CondicionUnitariaForm()
        negociacion_id = negociacion_id
        return render_to_response("negociacion/nuevo4.html", locals(), context_instance=RequestContext(request))

def listado(request):
    negociaciones=Negociacion.objects.filter(Q(complejo=request.user))
    usuario_registrado=UsuarioRegistrado.objects.get(pk=request.user.id)
    return render_to_response("negociacion/listado.html", locals(), context_instance=RequestContext(request))

def ver_negociacion_complejo(request,negociacion_id):
    if request.user.is_authenticated():
        usuario_registrado=UsuarioRegistrado.objects.get(pk=request.user.id)
    negociacion=Negociacion.objects.get(pk=negociacion_id)
    bandasMusicos=ComposicionBanda.objects.filter(musico_id=request.user.id)
    #negociacionesBanda=NegociacionBanda.objects.filter(negociacion_id=negociacion_id)
    nBandas=NegociacionBanda.objects.filter(negociacion_id=negociacion_id)    
    
    return render_to_response("negociacion/ver.html", locals(), context_instance=RequestContext(request))

#los musicos ven las negociaciones de todas las bandas a las que pertenecen!!!!
#Se agrega el group by para el caso en que un musico que pertenezca a dos bandas y la negociacion tenga linkeada esas dos bandas y que solo se le muestre una sola vez el evento!.
def ver_negociacion_banda(request):
    usuario_registrado=UsuarioRegistrado.objects.get(pk=request.user.id)
    estadoRechazado=EstadoNegociacion.objects.get(nombre="Rechazada")
    negociaciones=Negociacion.objects.raw('''select max(n.id) as id,n.nombre,n.inicio_negociacion,n.fecha,n.hora,n.complejo_id,n.sede_id,n.evento_id,n.monto,n.estado_id
                                        from negociacion n inner join negociacion_banda nb on (n.id = nb.negociacion_id)
                                            inner join banda b on (b.id = nb.banda_id)
                                            inner join composicion_banda cb on (b.id = cb.banda_id)
                                        where cb.musico_id = %s and nb.estado_id<>%s
                                        group by n.nombre,n.inicio_negociacion,n.fecha,n.hora,n.complejo_id,n.sede_id,n.evento_id,n.monto,n.estado_id
                                        ''',[request.user.id,estadoRechazado.id])                               
    return render_to_response("negociacion/listado.html", locals(), context_instance=RequestContext(request))

def confirmar_negociacion(request,negociacion_id):
    negociacion=Negociacion.objects.get(pk=negociacion_id)
    negociacion.estado=EstadoNegociacion.objects.get(nombre="Confirmada")
    negociacion.save()
    messages.success(request, 'Negociacion Confirmada con exito.')
    return HttpResponseRedirect(reverse('negociacion.views.ver_negociacion_banda'))

def rechazar_negociacion(request,negociacion_id):
    negociacion=Negociacion.objects.get(pk=negociacion_id)
    if negociacion.inicio_negociacion == "B":
        negociacion.estado=EstadoNegociacion.objects.get(nombre="Rechazada")
        negociacion.save()
    else:
        negociacion.delete()
    messages.success(request, 'Negociacion Rechazada con exito.')
    return HttpResponseRedirect(reverse('negociacion.views.ver_negociacion_banda'))

def confirmar_negociacion_banda(request,negociacion_id,negociacionBanda_id):
    negociacionBanda=NegociacionBanda.objects.get(pk=negociacionBanda_id)
    negociacionBanda.estado=EstadoNegociacion.objects.get(nombre="Confirmada")
    negociacionBanda.save()
    cantBandasNegociacionPendiente=NegociacionBanda.objects.filter(negociacion_id=negociacion_id,estado=EstadoNegociacion.objects.get(nombre="Pendiente")).count()
    if cantBandasNegociacionPendiente == 0:
        negociacion=Negociacion.objects.get(pk=negociacion_id)
        negociacion.estado=EstadoNegociacion.objects.get(nombre="Confirmada")
        negociacion.save()
        evento=Evento.objects.create(nombre=negociacion.nombre,fecha=negociacion.fecha,hora_inicio=negociacion.hora,
                                     complejo_id=negociacion.complejo_id,sede_id=negociacion.sede_id)
        evento.save()
        bandasParticipantes=NegociacionBanda.objects.filter(negociacion_id=negociacion_id)    
        for banda in bandasParticipantes:
            participacion = Participacion.objects.create(evento_id=evento.id, banda_id=banda.banda_id)
            #participacion.estado="A confirmar"
            participacion.save()      
    return HttpResponseRedirect(reverse('negociacion.views.ver_negociacion_banda'))

def rechazar_negociacion_banda(request,negociacion_id,negociacionBanda_id):    
    negociacionBanda=NegociacionBanda.objects.get(pk=negociacionBanda_id)
    negociacionBanda.estado=EstadoNegociacion.objects.get(nombre="Rechazada")
    negociacionBanda.save()
    cantBandasNegociacionPendiente=NegociacionBanda.objects.filter(negociacion_id=negociacion_id,estado=EstadoNegociacion.objects.get(nombre="Pendiente")).count()
    if cantBandasNegociacionPendiente == 0:
        negociacion=Negociacion.objects.get(pk=negociacion_id)
        negociacion.estado=EstadoNegociacion.objects.get(nombre="Rechazada")
        if negociacion.inicio_negociacion == "B":
            negociacion.delete()
        else:
            negociacion.save()
    return HttpResponseRedirect(reverse('negociacion.views.ver_negociacion_banda'))

    