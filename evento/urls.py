from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'^evento/nuevo', 'evento.views.evento_sin_negociacion'),
    url(r'^evento/listado', 'evento.views.listado'),
    url(r'^evento/(?P<evento_id>\d+)/ver', 'evento.views.ver'),
    url(r'^evento/(?P<evento_id>\d+)/asistir','evento.views.asistir'),
    url(r'^evento/(?P<evento_id>\d+)/no_asistir','evento.views.no_asistir'),
    
)