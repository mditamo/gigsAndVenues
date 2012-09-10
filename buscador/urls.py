from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'^buscador/index', 'buscador.views.index'),
)

