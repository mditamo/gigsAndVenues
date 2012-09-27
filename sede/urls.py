from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'^sede/listado$','sede.views.listado'),
    url(r'^sede/nuevo','sede.views.nuevo'),
    url(r'^sede/(?P<sede_id>\d+)/administrar/$','sede.views.administrar'),
    url(r'^sede/(?P<sede_id>\d+)/modificar/$','sede.views.modificar'),
    url(r'^sede/(?P<sede_id>\d+)/nueva_configuracion_sede/$','sede.views.nueva_configuracion_sede'),
    url(r'^configuracion_sede/(?P<configuracion_sede_id>\d+)/eliminar/$','sede.views.eliminar_configuracion_sede'),
    url(r'^configuracion_sede/(?P<configuracion_sede_id>\d+)/modificar/$','sede.views.modificar_configuracion_sede'),
    
    
)

