from django.conf.urls.defaults import *

urlpatterns = patterns('',
   url(r'^retiro_entrada/index$','entrada.views.retiro_entrada_index'),
   url(r'^retiro_entrada/(?P<reserva_entrada_id>\d+)/confirmar$','entrada.views.confirmar_retiro_entrada'),
   url(r'^evento/(?P<evento_id>\d+)/reservar_entrada','entrada.views.reservar_entrada'),
   url(r'^evento/(?P<evento_id>\d+)/eliminar_reserva_entrada','entrada.views.eliminar_reserva_entrada'),
   url(r'^entrada/listado','entrada.views.entrada_listado'),
   url(r'^esquema_entrada/evento/(?P<evento_id>\d+)/sede/(?P<sede_id>\d+)/seleccionar_configuracion_sede','entrada.views.seleccionar_configuracion_sede'),
   url(r'^esquema_entrada/evento/(?P<evento_id>\d+)/sede/(?P<sede_id>\d+)/listado','entrada.views.listado_esquema_entrada'),
   url(r'^esquema_entrada/evento/(?P<evento_id>\d+)/sede/(?P<sede_id>\d+)/configuracion_sede/(?P<configuracion_sede_id>\d+)/nuevo','entrada.views.nuevo_esquema_entrada'),
   url(r'^configuracion_esquema_entrada/(?P<configuracion_esquema_entrada_id>\d+)/modificar','entrada.views.modificar_esquema_entrada'),
   url(r'^configuracion_esquema_entrada/(?P<configuracion_esquema_entrada_id>\d+)/eliminar','entrada.views.eliminar_esquema_entrada'),
)