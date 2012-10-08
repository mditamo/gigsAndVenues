from django.conf.urls.defaults import *

urlpatterns = patterns('',
     url(r'^mapa/listado$', 'mapa.views.listado'),
     url(r'^mapa/id/(?P<evento_id>\d+)/ver$','mapa.views.ver'),
   
)

