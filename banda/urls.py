from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'^banda/(?P<banda_id>\d+)/ver/$','banda.views.ver'),
    url(r'^banda/(?P<banda_id>\d+)/administrar/$','banda.views.administrar'),
    url(r'^banda/nuevo/$','banda.views.nuevo'),
    url(r'^banda/listado$','banda.views.listado'),
    url(r'^banda/solicitud$','banda.views.solicitud'),
    url(r'^banda/(?P<banda_id>\d+)/confirmar_solicitud/$','banda.views.confirmar_solicitud'),
    url(r'^banda/(?P<banda_id>\d+)/modificar/$','banda.views.modificar'),
	url(r'^banda/(?P<banda_id>\d+)/invitar_musico/$','banda.views.invitar_musico'),
    url(r'^banda/(?P<banda_id>\d+)/musico/(?P<musico_id>\d+)/enviar_invitacion/$','banda.views.enviar_invitacion'),
    url(r'^banda/(?P<banda_id>\d+)/musico/(?P<musico_id>\d+)/confirmar/$','banda.views.confirmar'),
	url(r'^banda/(?P<banda_id>\d+)/musico/(?P<musico_id>\d+)/denegar/$','banda.views.denegar'),
	url(r'^banda/(?P<banda_id>\d+)/musico/(?P<musico_id>\d+)/modificar/$','banda.views.modificar_composicion_banda'),
	url(r'^banda/(?P<banda_id>\d+)/musico/(?P<musico_id>\d+)/eliminar/$','banda.views.eliminar'),
    url(r'^banda/(?P<banda_id>\d+)/like','banda.views.like'),
    url(r'^banda/(?P<banda_id>\d+)/no_like','banda.views.no_like'),
    url(r'^banda/(?P<banda_id>\d+)/suscribirme','banda.views.suscribirme'),
    url(r'^banda/(?P<banda_id>\d+)/no_suscribirme','banda.views.no_suscribirme'),
)

