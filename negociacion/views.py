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

def negociacionPaso1(request):
    usuario_registrado=UsuarioRegistrado.objects.get(pk=request.user.id)
    if request.method == 'POST':
        if usuario_registrado.is_complejo():
            form = NegociacionComplejoFormPaso1(request.POST)
            flag = 'C'
        else:
            form = NegociacionBandaFormPaso1(request.POST)
            flag = 'M'
        negociacion=form.save(commit=False)
        negociacion.inicio_negociacion = flag
        negociacion.complejo_id=request.user.id
        negociacion.estado=EstadoNegociacion.objects.get(nombre="Pendiente")
        if form.is_valid():
            negociacion.save()
        return HttpResponseRedirect(reverse('negociacion.views.negociacionPaso2', kwargs={'negociacion_id':negociacion.id}))
    else:
        if usuario_registrado.is_complejo():
            form = NegociacionComplejoFormPaso1()
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
        if form.is_valid():
            for banda_id in request.POST.getlist('bandas'):
                estadoBanda=EstadoNegociacion.objects.get(nombre="Pendiente")
                negociacionBanda = NegociacionBanda.objects.create(negociacion_id=negociacion_id, banda_id=banda_id,estado=estadoBanda)
                negociacionBanda.save()
        return HttpResponseRedirect(reverse('negociacion.views.negociacionPaso3', kwargs={'negociacion_id':negociacion_id}))
    else:
        if usuario_registrado.is_complejo():
            form = NegociacionComplejoFormPaso2()
        else:
            form = NegociacionBandaFormPaso2()
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
            negociacionTratada.fecha = negociacion.fecha 
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
    
    return render_to_response("negociacion/ver.html", locals(), context_instance=RequestContext(request))

#los musicos ven las negociaciones de todas las bandas a las que pertenecen!!!!
def ver_negociacion_banda(request):
    usuario_registrado=UsuarioRegistrado.objects.get(pk=request.user.id)
    negociaciones=Negociacion.objects.raw(''' select n.* 
                                        from negociacion n inner join negociacion_banda nb on (n.id = nb.negociacion_id)
                                            inner join banda b on (b.id = nb.banda_id)
                                            inner join composicion_banda cb on (b.id = cb.banda_id)
                                        where cb.musico_id = %s''',[request.user.id])
    bandasMusico=Banda.objects.raw(''' select b.* 
                                    from banda b inner join composicion_banda cb on (b.id = cb.id_banda)
                                    where cb.id_musico = %s''',[request.user.id])
                               
    return render_to_response("negociacion/listado.html", locals(), context_instance=RequestContext(request))

def confirmar_negociacion(request,negociacion_id):
    negociacion=Negociacion.objects.get(pk=negociacion_id)

    