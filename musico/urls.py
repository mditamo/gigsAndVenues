from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'^musico/perfil', 'musico.views.perfil'),
    url(r'^musico/(?P<musico_id>\d+)/modificar/$','musico.views.modificar'),
    url(r'^musico/(?P<musico_id>\d+)/ver/$','musico.views.ver'),
    url(r'^musico/equipos', 'musico.views.equipos'),
)
