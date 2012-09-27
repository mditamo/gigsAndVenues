from django.conf.urls.defaults import *


urlpatterns = patterns('',
    url(r'^fan/perfil', 'fan.views.perfil'),
    url(r'^fan/(?P<fan_id>\d+)/modificar/$','fan.views.modificar'),
    url(r'^fan/(?P<fan_id>\d+)/ver/$','fan.views.ver'),
)
