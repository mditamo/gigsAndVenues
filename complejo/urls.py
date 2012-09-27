from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'^complejo/perfil', 'complejo.views.perfil'),
    url(r'^complejo/(?P<complejo_id>\d+)/ver','complejo.views.ver'),
    url(r'^complejo/(?P<complejo_id>\d+)/modificar','complejo.views.modificar'),
    url(r'^complejo/(?P<complejo_id>\d+)/like','complejo.views.like'),
    url(r'^complejo/(?P<complejo_id>\d+)/no_like','complejo.views.no_like'),
    url(r'^complejo/nuevo_evento/sinNegociacion','evento.views.evento_sin_negociacion'),
	url(r'^complejo/(?P<complejo_id>\d+)/suscribirme','complejo.views.suscribirme'),
    url(r'^complejo/(?P<complejo_id>\d+)/no_suscribirme','complejo.views.no_suscribirme'),
)

