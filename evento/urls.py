from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'^evento/nuevo', 'evento.views.evento_sin_negociacion'),
    url(r'^evento/listado', 'evento.views.listado'),
)