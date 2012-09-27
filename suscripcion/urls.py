from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'^suscripcion/listado$','suscripcion.views.listado'),
    
    url(r'^suscripcion/genero/(?P<genero_id>\d+)/modificar','suscripcion.views.modificar_genero'),
    url(r'^suscripcion/genero/(?P<genero_id>\d+)/eliminar$','suscripcion.views.eliminar_genero'),
    
    url(r'^suscripcion/banda/(?P<banda_id>\d+)/modificar$','suscripcion.views.modificar_banda'),
    url(r'^suscripcion/banda/(?P<banda_id>\d+)/eliminar$','suscripcion.views.eliminar_banda'),
    
    url(r'^suscripcion/musico/(?P<musico_id>\d+)/modificar$','suscripcion.views.modificar_musico'),
    url(r'^suscripcion/musico/(?P<musico_id>\d+)/eliminar$','suscripcion.views.eliminar_musico'),
    
    url(r'^suscripcion/complejo/(?P<complejo_id>\d+)/modificar$','suscripcion.views.modificar_complejo'),
    url(r'^suscripcion/complejo/(?P<complejo_id>\d+)/eliminar$','suscripcion.views.eliminar_complejo'),
    
)

