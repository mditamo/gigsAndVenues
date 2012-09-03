from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'^equipo/listado', 'equipo.views.listado'),
    url(r'^equipo/nuevo', 'equipo.views.nuevo'),
    url(r'^equipo/(?P<equipo_musico_id>\d+)/modificar', 'equipo.views.modificar'),
    url(r'^equipo/(?P<equipo_musico_id>\d+)/eliminar', 'equipo.views.eliminar'),
)
