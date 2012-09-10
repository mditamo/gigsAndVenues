from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'^noticia/listado/$','noticia.views.listado'),
    url(r'^noticia_banda/banda/(?P<banda_id>\d+)/nuevo/$','noticia.views.nuevo_noticia_banda'),
    url(r'^noticia_banda/(?P<noticia_id>\d+)/ver/$','noticia.views.ver_noticia_banda'),
    url(r'^noticia_banda/(?P<noticia_id>\d+)/detalle/$','noticia.views.detalle_noticia_banda'),
    url(r'^noticia_banda/(?P<noticia_id>\d+)/modificar/$','noticia.views.modificar_noticia_banda'),
	url(r'^noticia_banda/(?P<noticia_id>\d+)/eliminar/$','noticia.views.eliminar_noticia_banda'),
    url(r'^noticia_banda/(?P<noticia_id>\d+)/publicar/$','noticia.views.publicar_noticia_banda'),
    url(r'^noticia_banda/(?P<noticia_id>\d+)/borrador/$','noticia.views.borrador_noticia_banda'),
    url(r'^noticia_banda/(?P<noticia_id>\d+)/archivar/$','noticia.views.archivar_noticia_banda'),
    url(r'^noticia_complejo/listado$','noticia.views.listado_noticia_complejo'),
    url(r'^noticia_complejo/nuevo','noticia.views.nuevo_noticia_complejo'),
    url(r'^noticia_complejo/(?P<noticia_id>\d+)/ver/$','noticia.views.ver_noticia_complejo'),
    url(r'^noticia_complejo/(?P<noticia_id>\d+)/modificar/$','noticia.views.modificar_noticia_complejo'),
    url(r'^noticia_complejo/(?P<noticia_id>\d+)/eliminar/$','noticia.views.eliminar_noticia_complejo'),
    url(r'^noticia_complejo/(?P<noticia_id>\d+)/publicar/$','noticia.views.publicar_noticia_complejo'),
    url(r'^noticia_complejo/(?P<noticia_id>\d+)/borrador/$','noticia.views.borrador_noticia_complejo'),
    url(r'^noticia_complejo/(?P<noticia_id>\d+)/archivar/$','noticia.views.archivar_noticia_complejo'),
    
)

