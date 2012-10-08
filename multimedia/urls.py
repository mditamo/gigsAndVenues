from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'^multimedia/banda/(?P<banda_id>\d+)/nuevo','multimedia.views.nuevo_recurso_multimedia_banda'),
    url(r'^multimedia_banda/(?P<recurso_multimedia_id>\d+)/modificar$','multimedia.views.modificar_recurso_multimedia_banda'),
    url(r'^multimedia_banda/(?P<recurso_multimedia_id>\d+)/eliminar$','multimedia.views.eliminar_recurso_multimedia_banda'),
    
    url(r'^multimedia/sede/(?P<sede_id>\d+)/nuevo$','multimedia.views.nuevo_recurso_multimedia_sede'),
    url(r'^multimedia_sede/(?P<recurso_multimedia_id>\d+)/modificar$','multimedia.views.modificar_recurso_multimedia_sede'),
    url(r'^multimedia_sede/(?P<recurso_multimedia_id>\d+)/eliminar$','multimedia.views.eliminar_recurso_multimedia_sede'),
    
)

