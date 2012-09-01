from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'^banda/(?P<banda_id>\d+)/ver/$','banda.views.ver'),
    url(r'^banda/nuevo/$','banda.views.nuevo'),
    url(r'^banda/(?P<banda_id>\d+)/modificar/$','banda.views.modificar'),
	url(r'^banda/(?P<banda_id>\d+)/musico/(?P<musico_id>\d+)/confirmar/$','banda.views.confirmar'),
	url(r'^banda/(?P<banda_id>\d+)/musico/(?P<musico_id>\d+)/denegar/$','banda.views.denegar'),
	url(r'^banda/(?P<banda_id>\d+)/musico/(?P<musico_id>\d+)/modificar/$','banda.views.modificar_composicion_banda'),
	url(r'^banda/(?P<banda_id>\d+)/musico/(?P<musico_id>\d+)/eliminar/$','banda.views.eliminar'),
)

