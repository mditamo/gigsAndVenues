from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'^tema/banda/(?P<banda_id>\d+)/nuevo/$','tema.views.nuevo'),
    url(r'^tema/(?P<tema_id>\d+)/banda/(?P<banda_id>\d+)/modificar/$','tema.views.modificar'),
)

