from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'^genero/(?P<genero_id>\d+)/ver$','genero.views.ver'),
    url(r'^genero/(?P<genero_id>\d+)/like','genero.views.like'),
    url(r'^genero/(?P<genero_id>\d+)/no_like','genero.views.no_like'),
)

