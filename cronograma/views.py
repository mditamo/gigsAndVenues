# Create your views here.
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template.context import RequestContext
from usuario.models import UsuarioRegistrado 
from evento.models import AsistenciaFan
from django.contrib.auth.decorators import login_required
from django.contrib import messages


@login_required(login_url='/usuario/login/')
def listado(request):
    if request.user.is_authenticated():
        usuario_registrado=UsuarioRegistrado.objects.get(pk=request.user.id)
    asistencias=AsistenciaFan.objects.filter(fan__id=request.user.id)    
    return render_to_response("cronograma/listado.html", locals(), context_instance=RequestContext(request))

