from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'^disco/(?P<disco_id>\d+)/ver/$','disco.views.ver'),
    url(r'^disco/(?P<disco_id>\d+)/administrar/$','disco.views.administrar'),
    url(r'^disco/banda/(?P<banda_id>\d+)/nuevo/$','disco.views.nuevo'),
    url(r'^disco/(?P<disco_id>\d+)/modificar/$','disco.views.modificar'),
	url(r'^disco/(?P<disco_id>\d+)/eliminar/$','disco.views.eliminar'),
    url(r'^disco/(?P<disco_id>\d+)/nuevo_composicion_disco/$','disco.views.nuevo_composicion_disco'),
    url(r'^composicion_disco/(?P<composicion_disco_id>\d+)/modificar/$','disco.views.modificar_composicion_disco'),
    url(r'^composicion_disco/(?P<composicion_disco_id>\d+)/eliminar/$','disco.views.eliminar_composicion_disco'),
)

