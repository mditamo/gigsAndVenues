from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'^complejo/perfil', 'complejo.views.perfil'),
    url(r'^complejo/(?P<complejo_id>\d+)/ver','complejo.views.ver'),
    url(r'^complejo/(?P<complejo_id>\d+)/modificar','complejo.views.modificar'),
    url(r'^complejo/(?P<complejo_id>\d+)/like','complejo.views.like'),
    url(r'^complejo/(?P<complejo_id>\d+)/no_like','complejo.views.no_like'),
)
