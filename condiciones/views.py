from django.template.context import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from usuario.models import UsuarioRegistrado
from negociacion.models import CondicionNegociacion
from condiciones.forms import CondicionUnitariaForm

def agregarCondicion(request,negociacion_id):
    usuario_registrado=UsuarioRegistrado.objects.get(pk=request.user.id)
    if request.method == 'POST':
        form = CondicionUnitariaForm(request.POST)              
        condicion=form.save(commit=False)      
        if form.is_valid():
            condicion.save()
            condicionNegociacion = CondicionNegociacion.objects.create(negociacion_id=negociacion_id, condicionUnitaria_id=condicion.id)
            condicionNegociacion.save()
            if request.POST.get('submit')=='Agregar':
                form = CondicionUnitariaForm()
                negociacion_id = negociacion_id
                return render_to_response("negociacion/nuevo4.html", locals(), context_instance=RequestContext(request))
            else:    
                return HttpResponseRedirect(reverse('negociacion.views.listado'))
    else:
        form = CondicionUnitariaForm()
        negociacion_id = negociacion_id
        return render_to_response("negociacion/nuevo4.html", locals(), context_instance=RequestContext(request))