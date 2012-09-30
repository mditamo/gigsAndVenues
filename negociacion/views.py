from django.template.context import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from usuario.models import UsuarioRegistrado
from negociacion.forms import NegociacionComplejoFormPaso1,NegociacionBandaFormPaso1
from negociacion.forms import NegociacionComplejoFormPaso2,NegociacionBandaFormPaso2
from negociacion.forms import NegociacionComplejoFormPaso3,NegociacionBandaFormPaso3
from django.db.models import Q
from negociacion.models import Negociacion
from sede.models import Sede


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
            obj = Negociacion.objects.get(pk=negociacion_id)
            obj.banda_id = negociacion.banda_id 
            obj.save()
        #return HttpResponseRedirect(reverse('negociacion.views.listado'))
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
            obj = Negociacion.objects.get(pk=negociacion_id)
            obj.fecha = negociacion.fecha 
            obj.save()
        #return HttpResponseRedirect(reverse('negociacion.views.listado'))
        return HttpResponseRedirect(reverse('negociacion.views.negociacionPaso3', kwargs={'negociacion_id':negociacion.id}))
    else:
        if usuario_registrado.is_complejo():
            form = NegociacionComplejoFormPaso3()
        else:
            form = NegociacionBandaFormPaso3()
        return render_to_response("negociacion/nuevo2.html", locals(), context_instance=RequestContext(request))

def listado(request):
    negociaciones=Negociacion.objects.filter(Q(complejo=request.user))
    usuario_registrado=UsuarioRegistrado.objects.get(pk=request.user.id)
    return render_to_response("negociacion/listado.html", locals(), context_instance=RequestContext(request))