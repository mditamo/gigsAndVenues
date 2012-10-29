from django.template.context import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from usuario.models import UsuarioRegistrado
from negociacion.models import CondicionNegociacion,NegociacionBanda,Negociacion,\
    EstadoNegociacion
from condiciones.forms import CondicionUnitariaForm, verCondicionUnitariaForm
from condiciones.models import CondicionUnitaria
from django.forms.models import modelformset_factory
from oferta.models import Oferta,CondicionOferta
from django.contrib import messages


def agregarCondicion(request,negociacion_id):
    usuario_registrado=UsuarioRegistrado.objects.get(pk=request.user.id)
    if request.method == 'POST':
        form = CondicionUnitariaForm(request.POST)              
        condicion=form.save(commit=False)      
        if form.is_valid():
            condicion.negociacion_id=negociacion_id
            condicion.save()
            condicionNegociacion = CondicionNegociacion.objects.create(negociacion_id=negociacion_id, condicionUnitaria_id=condicion.id)
            condicionNegociacion.save()
            if request.POST.get('submit')=='Agregar':
                form = CondicionUnitariaForm()
                negociacion_id = negociacion_id
                return render_to_response("condicion/crear_condicion.html", locals(), context_instance=RequestContext(request))
            else:    
                return HttpResponseRedirect(reverse('negociacion.views.listado'))
    else:
        form = CondicionUnitariaForm()
        negociacion_id = negociacion_id
        #return render_to_response("negociacion/nuevo4.html", locals(), context_instance=RequestContext(request))
        return render_to_response("condicion/crear_condicion.html", locals(), context_instance=RequestContext(request))

def verCondiciones(request,negociacion_id,negociacionBanda_id):
    usuario_registrado=UsuarioRegistrado.objects.get(pk=request.user.id)
    existenCambios=False
    ofertas=Oferta.objects.filter(negociacion_id=negociacion_id)
    lengthOfertas=len(ofertas)
    
    ModelFormSet=modelformset_factory(CondicionUnitaria,exclude = ('negociacion_id','oferta_id',),extra=0)                          
    if request.method =='POST':
        if lengthOfertas == 0:
            formset=ModelFormSet(request.POST,request.FILES,prefix='condicionesIniciales',queryset=CondicionUnitaria.objects.filter(negociacion_id=negociacion_id))
        elif lengthOfertas == 1:    
            formsetInicial=ModelFormSet(request.POST,request.FILES,prefix='condicionesIniciales',queryset=CondicionUnitaria.objects.filter(negociacion_id=negociacion_id,oferta_id__isnull = True))
            formset=ModelFormSet(request.POST,request.FILES,prefix='condiciones',queryset=CondicionUnitaria.objects.filter(negociacion_id=negociacion_id,oferta__is_ultima_oferta=1))
        elif lengthOfertas > 1:
            formsetInicial=ModelFormSet(request.POST,request.FILES,prefix='condicionesIniciales',queryset=CondicionUnitaria.objects.filter(negociacion_id=negociacion_id,oferta__is_penultima_oferta=1))    
            formset=ModelFormSet(request.POST,request.FILES,prefix='condiciones',queryset=CondicionUnitaria.objects.filter(negociacion_id=negociacion_id,oferta__is_ultima_oferta=1))
    
        if usuario_registrado.is_musico():
            usuario_oferta='B'
        if usuario_registrado.is_complejo():
            usuario_oferta='C'
        
        if lengthOfertas > 0:
            ultimaOferta=Oferta.objects.get(is_ultima_oferta=1,negociacion_id=negociacion_id)
        
        
        if lengthOfertas > 0 and ultimaOferta.usuario_oferta==usuario_oferta:
            messages.success(request, 'No puede realizar nueva oferta ya que la ultima generada es suya.')
        else:
            
            #formsetInicial=formset(request.POST,request.FILES,prefix='condicionesIniciales')
            condicionesIni=CondicionUnitaria.objects.filter(negociacion_id=negociacion_id)
            negociacionBanda=NegociacionBanda.objects.get(pk=negociacionBanda_id)
            negociacionTratada=Negociacion.objects.get(pk=negociacionBanda.negociacion_id)
            flag_id=9999999999
            if formset.is_valid:
                #formset.save()
                for form in formset:
                    form.negociacion_id=negociacion_id
                    condicion=form.save(commit=False)               
                    nueva=CondicionUnitaria.objects.create(descripcion=condicion.descripcion,tipoCondicion=condicion.tipoCondicion,
                                                           valor=condicion.valor,negociacion_id=negociacion_id,oferta_id=flag_id)
                    nueva.save()
                    #condicion.save()
                    estadoOferta=EstadoNegociacion.objects.get(nombre="Pendiente")
                    condicionOferta=CondicionOferta.objects.create(oferta_id=flag_id,condicionUnitaria_id=nueva.id)
                    condicionOferta.save()
                
                if(lengthOfertas>0):    
                    penultimaOferta=Oferta.objects.get(negociacion_id=negociacion_id,banda=negociacionBanda.banda,
                                                          complejo=negociacionTratada.complejo,sede=negociacionTratada.sede,
                                                          is_ultima_oferta=True)
                
                    if(lengthOfertas>1):
                        antePenultimaOferta=Oferta.objects.get(negociacion_id=negociacion_id,banda=negociacionBanda.banda,
                                                               complejo=negociacionTratada.complejo,sede=negociacionTratada.sede,
                                                               usuario_oferta=usuario_oferta,is_penultima_oferta=True)
                        
                        antePenultimaOferta.is_penultima_oferta=False
                        antePenultimaOferta.save()
                    
                    penultimaOferta.is_ultima_oferta=False;
                    penultimaOferta.is_penultima_oferta=True;
                    penultimaOferta.save()
                    
                oferta=Oferta.objects.create(negociacion_id=negociacion_id,banda=negociacionBanda.banda,
                                             complejo=negociacionTratada.complejo,sede=negociacionTratada.sede,
                                             usuario_oferta=usuario_oferta,is_ultima_oferta=True,estado=estadoOferta)
                oferta.save()
    
                #Debo actualizar las condiciones unitarias 
                condicionesUnitarias=CondicionUnitaria.objects.filter(negociacion_id=negociacion_id, oferta_id=flag_id)
                for condicion in condicionesUnitarias:
                    condicion.oferta_id=oferta.id
                    condicion.save()
                
                condicionesOferta=CondicionOferta.objects.filter(oferta_id=flag_id)
                for condicionOferta in condicionesOferta:                    
                    condicionOferta.oferta_id=oferta.id
                    condicionOferta.save()            
        return HttpResponseRedirect(reverse('negociacion.views.listado'))
    else:
        if lengthOfertas==0:  
            formset=ModelFormSet(prefix='condicionesIniciales',queryset=CondicionUnitaria.objects.filter(negociacion_id=negociacion_id))
            return render_to_response("condicion/ver_condicion.html", locals(), context_instance=RequestContext(request))
        elif lengthOfertas==1:
            formsetInicial=ModelFormSet(prefix='condicionesIniciales',queryset=CondicionUnitaria.objects.filter(negociacion_id=negociacion_id,oferta_id__isnull = True))
            formset=ModelFormSet(prefix='condiciones',queryset=CondicionUnitaria.objects.filter(negociacion_id=negociacion_id,oferta__is_ultima_oferta=1))
            
            for form in formsetInicial:
                form.fields['descripcion'].widget.attrs['disabled'] = True
                form.fields['tipoCondicion'].widget.attrs['disabled'] = True
                form.fields['valor'].widget.attrs['disabled'] = True 
            return render_to_response("condicion/ver_condicion.html", locals(), context_instance=RequestContext(request))
        elif lengthOfertas > 1: 
            formsetInicial=ModelFormSet(prefix='condicionesIniciales',queryset=CondicionUnitaria.objects.filter(negociacion_id=negociacion_id,oferta__is_penultima_oferta=1))    
            formset=ModelFormSet(prefix='condiciones',queryset=CondicionUnitaria.objects.filter(negociacion_id=negociacion_id,oferta__is_ultima_oferta=1))

            for form in formsetInicial:
                form.fields['descripcion'].widget.attrs['disabled'] = True
                form.fields['tipoCondicion'].widget.attrs['disabled'] = True
                form.fields['valor'].widget.attrs['disabled'] = True             
            return render_to_response("condicion/ver_condicion.html", locals(), context_instance=RequestContext(request))
                
                
                