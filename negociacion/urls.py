from django.conf.urls.defaults import *
urlpatterns = patterns('',
    url(r'^negociacion/nuevo/paso1', 'negociacion.views.negociacionPaso1'),
    url(r'^negociacion/nuevo/paso2', 'negociacion.views.negociacionPaso2'),
    url(r'^negociacion/listado', 'negociacion.views.listado'),
    url(r'^negociacion/(?P<negociacion_id>\d+)/paso2/$','negociacion.views.negociacionPaso2'),
    url(r'^negociacion/(?P<negociacion_id>\d+)/paso3/$','negociacion.views.negociacionPaso3'),
    url(r'^negociacion/(?P<negociacion_id>\d+)/paso4/$','condiciones.views.agregarCondicion'),
    url(r'^negociacion/(?P<negociacion_id>\d+)/confirmar/$','negociacion.views.confirmar_negociacion'),
    url(r'^negociacion/(?P<negociacion_id>\d+)/rechazar/$','negociacion.views.rechazar_negociacion'),
    url(r'^negociacion/(?P<negociacion_id>\d+)/ver/$','negociacion.views.ver_negociacion_complejo'),
    #url(r'^negociacion/(?P<negociacion_id>\d+)/generarOferta/$','negociacion.views.generarOferta'),
    url(r'^negociacion/negociacion_banda/listado','negociacion.views.ver_negociacion_banda'),
)
