from django.template.context import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from usuario.models import UsuarioRegistrado
from negociacion.models import Negociacion
from condiciones.forms import CondicionUnitariaForm
from condiciones.models import CondicionUnitaria
from oferta.forms import generarOfertaForm


def generarOferta(request,negociacion_id):
    usuario_registrado=UsuarioRegistrado.objects.get(pk=request.user.id)
    negociacionTratada=Negociacion.objects.get(pk=negociacion_id)
    if request.method == 'POST':   
        return HttpResponseRedirect(reverse('negociacion.views.negociacionPaso2', kwargs={'negociacion_id':negociacion_id}))
    else:
        valores=CondicionUnitaria.objects.get(pk=1)
        #form = CondicionUnitariaForm(instance=valores)
        form = CondicionUnitariaForm()
        #return render_to_response("negociacion/nuevo.html", locals(), context_instance=RequestContext(request))
        return render_to_response("condicion/crear_condicion.html", locals(), context_instance=RequestContext(request))