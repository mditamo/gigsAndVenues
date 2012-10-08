from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'^celular/noticia/listado/$','celular.views.noticia_listado'),
    url(r'^celular/evento/listado/$','celular.views.evento_listado'),
    url(r'^celular/usuario/login/$','celular.views.usuario_login'),
    url(r'^celular/noticia_complejo/(?P<noticia_id>\d+)/ver/$','celular.views.ver_noticia_complejo'),
    url(r'^celular/noticia_banda/(?P<noticia_id>\d+)/ver/$','celular.views.ver_noticia_banda'),
    
)

