from django.http import HttpResponse
from UserString import MutableString
from evento.models import AsistenciaFan, Evento

def listado(request):
    
    out_str = MutableString()
    out_str += "<?xml version='1.0' encoding='utf-8'?>"
    asistencias=AsistenciaFan.objects.filter(fan__id=request.user.id) 
    if asistencias.count() > 0:
        out_str += "<markers>"
        for asistencia in asistencias:
            out_str += '<marker id="%(evento)s" address="%(sede)s" type="restaurant"/>' % {'evento':asistencia.evento.id,'sede':asistencia.evento.direccion_sede()}
        out_str += "</markers>" 
    mimetype = 'application/xml'
    return HttpResponse(out_str,mimetype)


def ver(request,evento_id):
    evento=Evento.objects.get(pk=evento_id)
    out_str = MutableString()
    out_str += "<?xml version='1.0' encoding='utf-8'?>"
    out_str += "<markers>"
    out_str += '<marker nombre_sede="%(nombre_sede)s" nombre_evento="%(nombre_evento)s" src_imagen="%(src_imagen)s" fecha="%(fecha)s" hora="%(hora)s"/>' % {'nombre_sede':evento.sede.nombre,'nombre_evento':evento.nombre, 'src_imagen':evento.sede.imagen_avatar(), 'fecha': evento.fecha, 'hora': evento.hora_inicio}
    out_str += "</markers>"
    mimetype = 'application/xml'
    return HttpResponse(out_str,mimetype)