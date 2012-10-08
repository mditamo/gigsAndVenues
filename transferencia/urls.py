from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'^transferencia/index', 'transferencia.views.index'),
    url(r'^transferencia/fan', 'transferencia.views.fan'),
    url(r'^transferencia/musico', 'transferencia.views.musico'),
    url(r'^transferencia/complejo', 'transferencia.views.complejo'),
)

