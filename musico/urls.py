from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'^musico/perfil', 'musico.views.perfil'),
    url(r'^musico/(?P<musico_id>\d+)/modificar/$','musico.views.modificar'),
    url(r'^musico/(?P<musico_id>\d+)/ver/$','musico.views.ver'),
    url(r'^musico/(?P<musico_id>\d+)/like','musico.views.like'),
    url(r'^musico/(?P<musico_id>\d+)/no_like','musico.views.no_like'),
    url(r'^musico/(?P<musico_id>\d+)/suscribirme','musico.views.suscribirme'),
    url(r'^musico/(?P<musico_id>\d+)/no_suscribirme','musico.views.no_suscribirme'),
)
